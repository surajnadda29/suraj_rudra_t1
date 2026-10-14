
from pathlib import Path
import json
import numpy as np
import pandas as pd

# Project folders
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent.parent

NOTES_DIR = PROJECT_DIR / "Day-11" / "codes"
LOGS_DIR = PROJECT_DIR / "Day-11" / "codes"

NOTES_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Sensor columns and illustrative valid ranges
SENSOR_LIMITS = {
    "temperature": (-50, 120),
    "pressure": (100, 1200),
    "altitude": (-500, 10000),
    "speed": (0, 200),
}


def load_telemetry():
    """Load an earlier telemetry dataset if available."""
    possible_files = [
        PROJECT_DIR / "Day7" / "codes"
        / "synthetic_uav_flight_telemetry.csv",
        ]

    for file_path in possible_files:
        if file_path.exists():
            print(f"Loading dataset: {file_path}")
            return pd.read_csv(file_path)

    # Create a small synthetic dataset if no earlier dataset exists.
    print("Previous dataset not found. Creating demo telemetry.")

    rng = np.random.default_rng(42)
    rows = 1000

    return pd.DataFrame({
        "timestamp": pd.date_range(
            "2026-10-15 09:00:00",
            periods=rows,
            freq="s"
        ),
        "sensor_id": ["SENSOR_01"] * rows,
        "temperature": rng.normal(35, 3, rows),
        "pressure": rng.normal(1000, 15, rows),
        "altitude": rng.normal(500, 30, rows),
        "speed": rng.normal(60, 8, rows),
    })


def inject_test_faults(data):
    """Add controlled faults to test the recovery process."""
    faulty = data.copy()

    for column in SENSOR_LIMITS:
        if column in faulty.columns:
            faulty[column] = pd.to_numeric(
                faulty[column], errors="coerce"
            )

    if len(faulty) > 31:
        faulty.loc[10, "temperature"] = np.nan
        faulty.loc[20, "altitude"] = np.nan
        faulty.loc[30, "temperature"] = 9999
        faulty.loc[31, "speed"] = -999

    return faulty


def recover_telemetry(faulty):
    """Detect invalid readings and interpolate internal gaps."""
    recovered = faulty.copy()
    report = {}

    for column, (minimum, maximum) in SENSOR_LIMITS.items():
        if column not in recovered.columns:
            continue

        original = pd.to_numeric(
            recovered[column], errors="coerce"
        )

        missing_before = int(original.isna().sum())

        invalid_mask = (
            original.notna()
            & (
                (original < minimum)
                | (original > maximum)
            )
        )

        invalid_count = int(invalid_mask.sum())

        # Mark out-of-range values as missing.
        cleaned = original.mask(invalid_mask)

        # Fill only gaps surrounded by valid readings.
        interpolated = cleaned.interpolate(
            method="linear",
            limit_area="inside"
        )

        missing_after = int(interpolated.isna().sum())

        recovered[column] = interpolated

        report[column] = {
            "missing_before": missing_before,
            "invalid_readings_detected": invalid_count,
            "missing_after_recovery": missing_after,
            "recovered_readings": int(
                cleaned.isna().sum() - missing_after
            ),
            "valid_range": [minimum, maximum],
        }

    return recovered, report


def main():
    original = load_telemetry()

    if "timestamp" in original.columns:
        original["timestamp"] = pd.to_datetime(
            original["timestamp"], errors="coerce"
        )
        original = original.sort_values(
            "timestamp"
        ).reset_index(drop=True)

    faulty = inject_test_faults(original)
    recovered, report = recover_telemetry(faulty)

    # Save the recovered data and a concise summary.
    output_file = NOTES_DIR / "recovered_telemetry.csv"
    report_file = LOGS_DIR / "recovery_summary.json"

    recovered.to_csv(output_file, index=False)

    summary = {
        "task": "Telemetry Fault Recovery",
        "input_rows": int(len(original)),
        "sensor_results": report,
        "method": "Range validation and linear interpolation",
        "limitations": [
            "Sensor limits are illustrative, not certified UAV limits.",
            "Interpolated values are estimates, not confirmed measurements.",
            "Gaps at the beginning or end may remain missing.",
            "This demonstration may use synthetic telemetry."
        ],
    }

    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("\n--- Telemetry Fault Recovery Summary ---")
    print(f"Total rows: {len(recovered)}")

    for sensor, details in report.items():
        print(f"\nSensor: {sensor}")
        print(
            "Invalid readings detected:",
            details["invalid_readings_detected"]
        )
        print(
            "Readings recovered:",
            details["recovered_readings"]
        )
        print(
            "Missing values remaining:",
            details["missing_after_recovery"]
        )

    print(f"\nRecovered data saved to: {output_file}")
    print(f"Summary saved to: {report_file}")


if __name__ == "__main__":
    main()
