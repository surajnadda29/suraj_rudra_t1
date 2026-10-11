
import json
import logging
import random
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pandas as pd

# All files stay inside Day8/codes
BASE_DIR = Path(__file__).resolve().parent

SOURCE_FILE = BASE_DIR / "synthetic_sensor_dataset.csv"
PROCESSED_FILE = BASE_DIR / "processed_telemetry.csv"
REJECTED_FILE = BASE_DIR / "rejected_telemetry.csv"
SUMMARY_FILE = BASE_DIR / "pipeline_summary.json"
LOG_FILE = BASE_DIR / "etl_pipeline.log"

NUMERIC_COLUMNS = [
    "temperature_c",
    "pressure_hpa",
    "altitude_m",
    "speed_mps",
    "battery_v",
]

EXPECTED_PHASES = {"ascent", "cruise", "descent"}


def generate_dataset(rows=250):
    """Generate a fresh, independent Day 8 dataset."""
    rng = random.Random(42)
    start = datetime(2026, 10, 12, 9, 0, tzinfo=timezone.utc)
    records = []

    for i in range(rows):
        if i < 80:
            phase = "ascent"
        elif i < 180:
            phase = "cruise"
        else:
            phase = "descent"

        if phase == "ascent":
            altitude = 100 + i * 8
            speed = 16
        elif phase == "cruise":
            altitude = 1500 + rng.uniform(-30, 30)
            speed = 24
        else:
            altitude = max(80, 1700 - (i - 180) * 14)
            speed = 13

        records.append({
            "record_id": i + 1,
            "timestamp": (
                start + timedelta(seconds=i * 5)
            ).isoformat(),
            "sensor_id": f"SENSOR-{(i % 4) + 1:02d}",
            "flight_phase": phase,
            "temperature_c": round(
                18 + altitude * 0.001 + rng.gauss(0, 0.8), 2
            ),
            "pressure_hpa": round(
                1013.25 - altitude * 0.036 + rng.gauss(0, 0.7), 2
            ),
            "altitude_m": round(
                altitude + rng.gauss(0, 2), 2
            ),
            "speed_mps": round(speed + rng.gauss(0, 1.2), 2),
            "battery_v": round(
                12.4 - i * 0.001 + rng.gauss(0, 0.04), 2
            ),
        })

    df = pd.DataFrame(records)

    # Add sample quality problems to test validation.
    df.loc[5, "temperature_c"] = None
    df.loc[12, "timestamp"] = "invalid-time"
    df.loc[20, "speed_mps"] = -7.5
    df.loc[30, "flight_phase"] = "unknown"
    df.loc[40, "sensor_id"] = ""
    df.loc[50, "altitude_m"] = float("inf")
    df.loc[60, "record_id"] = df.loc[59, "record_id"]

    df.to_csv(SOURCE_FILE, index=False)
    print(f"GENERATE: {len(df)} records created")
    return df


def extract_data():
    """Read the generated CSV into a DataFrame."""
    df = pd.read_csv(SOURCE_FILE)
    print(f"EXTRACT: {len(df)} records loaded")
    return df


def validate_data(df):
    """Separate valid rows from rejected rows."""
    required = [
        "record_id", "timestamp", "sensor_id", "flight_phase",
        *NUMERIC_COLUMNS
    ]

    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    work = df.copy()
    reasons = {idx: [] for idx in work.index}

    def mark(mask, reason):
        mask = mask.fillna(True)
        for idx in work.index[mask]:
            reasons[idx].append(reason)

    # Timestamp validation
    parsed_time = pd.to_datetime(
        work["timestamp"], errors="coerce", utc=True
    )
    mark(parsed_time.isna(), "invalid_timestamp")
    work["timestamp"] = parsed_time

    # Unique record IDs
    mark(work["record_id"].isna(), "missing_record_id")
    mark(
        work["record_id"].duplicated(keep=False),
        "duplicate_record_id"
    )

    # Sensor ID validation
    sensor = work["sensor_id"].astype("string").str.strip()
    mark(sensor.isna() | sensor.eq(""), "missing_sensor_id")
    work["sensor_id"] = sensor

    # Flight phase validation
    phase = (
        work["flight_phase"].astype("string").str.strip().str.lower()
    )
    mark(
        phase.isna() | ~phase.isin(EXPECTED_PHASES),
        "invalid_flight_phase"
    )
    work["flight_phase"] = phase

    # Numeric values and finite numbers
    for col in NUMERIC_COLUMNS:
        numeric = pd.to_numeric(work[col], errors="coerce")
        mark(numeric.isna(), f"missing_or_non_numeric_{col}")
        mark(
            numeric.isin([float("inf"), float("-inf")]),
            f"non_finite_{col}"
        )
        work[col] = numeric

    # Basic range checks
    mark(work["speed_mps"] < 0, "negative_speed")
    mark(work["battery_v"] <= 0, "invalid_battery_voltage")
    mark(work["pressure_hpa"] <= 0, "invalid_pressure")
    mark(work["altitude_m"] < 0, "negative_altitude")

    reason_series = pd.Series(
        {
            idx: ";".join(dict.fromkeys(items))
            for idx, items in reasons.items()
        },
        dtype="string",
    ).reindex(work.index)

    rejected_mask = reason_series.ne("")
    rejected = work.loc[rejected_mask].copy()
    rejected["rejection_reason"] = reason_series[rejected_mask]

    accepted = work.loc[~rejected_mask].copy()

    print(f"VALIDATE: accepted={len(accepted)}, rejected={len(rejected)}")
    return accepted, rejected


def process_data(accepted):
    """Sort, standardize types, and add elapsed time."""
    df = accepted.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df["record_id"] = df["record_id"].astype("int64")

    for col in NUMERIC_COLUMNS:
        df[col] = df[col].astype("float64")

    df = df.sort_values(
        ["timestamp", "record_id"]
    ).reset_index(drop=True)

    if not df.empty:
        first_time = df["timestamp"].min()
        df["elapsed_seconds"] = (
            df["timestamp"] - first_time
        ).dt.total_seconds()
    else:
        df["elapsed_seconds"] = pd.Series(dtype="float64")

    df["quality_status"] = "accepted"
    print(f"PROCESS: {len(df)} records processed")
    return df


def store_outputs(source, processed, rejected, runtime):
    """Save all pipeline outputs in the codes folder."""
    processed.to_csv(PROCESSED_FILE, index=False)
    rejected.to_csv(REJECTED_FILE, index=False)

    phase_counts = (
        processed["flight_phase"].value_counts().to_dict()
        if not processed.empty else {}
    )

    summary = {
        "pipeline_version": "v1",
        "execution_status": "SUCCESS",
        "source_records": int(len(source)),
        "accepted_records": int(len(processed)),
        "rejected_records": int(len(rejected)),
        "runtime_seconds": round(runtime, 4),
        "flight_phase_counts": {
            str(key): int(value)
            for key, value in phase_counts.items()
        },
        "outputs": [
            SOURCE_FILE.name,
            PROCESSED_FILE.name,
            REJECTED_FILE.name,
            SUMMARY_FILE.name,
            LOG_FILE.name,
        ],
        "note": "Synthetic demonstration data, not real flight data.",
    }

    SUMMARY_FILE.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print("STORE: CSV and JSON outputs saved")
    return summary


def main():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        force=True,
    )

    start = datetime.now(timezone.utc)
    logging.info("ETL Pipeline v1 started")

    # 1. Generate independent Day 8 data
    generate_dataset()

    # 2. Extract source data
    source = extract_data()

    # 3. Validate and split rows
    accepted, rejected = validate_data(source)

    # 4. Process accepted records
    processed = process_data(accepted)

    runtime = (
        datetime.now(timezone.utc) - start
    ).total_seconds()

    # 5. Store the results
    summary = store_outputs(
        source, processed, rejected, runtime
    )

    logging.info("ETL Pipeline v1 completed successfully")

    print("\n--- ETL PIPELINE v1 SUMMARY ---")
    print("Source records  :", summary["source_records"])
    print("Accepted records:", summary["accepted_records"])
    print("Rejected records:", summary["rejected_records"])
    print("Runtime (sec)   :", summary["runtime_seconds"])
    print("Saved in        :", BASE_DIR)


if __name__ == "__main__":
    main()
