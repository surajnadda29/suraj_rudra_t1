
import csv
import math
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Day 7: Synthetic UAV Flight Telemetry Generation
# All data is simulated for software testing, not real flight use.

random.seed(42)

OUTPUT_FILE = Path(__file__).parent / "synthetic_uav_flight_telemetry.csv"
TOTAL_RECORDS = 1000
SAMPLE_INTERVAL_SECONDS = 1

FIELDNAMES = [
    "timestamp",
    "sensor_id",
    "flight_phase",
    "temperature",
    "pressure",
    "altitude",
    "speed",
    "temperature_noise",
    "pressure_noise",
    "altitude_noise",
    "speed_noise",
    "status_mask",
]


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def generate_dataset():
    start_time = datetime.now(timezone.utc).replace(microsecond=0)

    # Slowly changing, correlated sensor drift states.
    drift = {
        "temperature": 0.0,
        "pressure": 0.0,
        "altitude": 0.0,
        "speed": 0.0,
    }

    drift_strength = {
        "temperature": 0.85,
        "pressure": 0.85,
        "altitude": 0.90,
        "speed": 0.85,
    }

    drift_scale = {
        "temperature": 0.08,
        "pressure": 0.25,
        "altitude": 0.35,
        "speed": 0.12,
    }

    white_noise_scale = {
        "temperature": 0.25,
        "pressure": 0.80,
        "altitude": 1.20,
        "speed": 0.45,
    }

    records = []

    for index in range(TOTAL_RECORDS):
        elapsed = index * SAMPLE_INTERVAL_SECONDS
        timestamp = start_time + timedelta(seconds=elapsed)
        progress = index / max(TOTAL_RECORDS - 1, 1)

        # Illustrative flight phases: ascent, cruise, descent.
        if progress < 0.35:
            flight_phase = "ascent"
            phase_progress = progress / 0.35
            base_altitude = 100 + 400 * phase_progress
            base_speed = 35 + 15 * phase_progress

        elif progress < 0.75:
            flight_phase = "cruise"
            phase_progress = (progress - 0.35) / 0.40
            base_altitude = 500 + 8 * math.sin(phase_progress * 2 * math.pi)
            base_speed = 50 + 2 * math.sin(phase_progress * 2 * math.pi)

        else:
            flight_phase = "descent"
            phase_progress = (progress - 0.75) / 0.25
            base_altitude = 500 - 400 * phase_progress
            base_speed = 50 - 12 * phase_progress

        # Simplified synthetic environmental baselines.
        base_temperature = 25 - 0.006 * base_altitude
        base_pressure = 1013.25 * math.exp(-base_altitude / 8434.5)

        baselines = {
            "temperature": base_temperature,
            "pressure": base_pressure,
            "altitude": base_altitude,
            "speed": base_speed,
        }

        measured = {}
        noise_values = {}

        for name, baseline in baselines.items():
            # Model 1: white Gaussian measurement noise.
            white_noise = random.gauss(0, white_noise_scale[name])

            # Model 2: slowly varying, correlated sensor drift.
            drift[name] = (
                drift_strength[name] * drift[name]
                + random.gauss(0, drift_scale[name])
            )

            # Model 3: occasional small, bounded disturbance.
            disturbance = 0.0
            if random.random() < 0.02:
                disturbance = random.uniform(
                    -2 * white_noise_scale[name],
                    2 * white_noise_scale[name],
                )

            total_noise = white_noise + drift[name] + disturbance
            noise_values[name] = round(total_noise, 4)
            measured[name] = round(baseline + total_noise, 3)

        # Demonstration status only; not calculated from sensor checks.
        status_mask = 15

        record = {
            "timestamp": timestamp.isoformat(),
            "sensor_id": "UAV_SENSOR_SUITE_001",
            "flight_phase": flight_phase,
            "temperature": measured["temperature"],
            "pressure": round(max(measured["pressure"], 0.1), 3),
            "altitude": round(max(measured["altitude"], 0.0), 3),
            "speed": round(max(measured["speed"], 0.0), 3),
            "temperature_noise": noise_values["temperature"],
            "pressure_noise": noise_values["pressure"],
            "altitude_noise": noise_values["altitude"],
            "speed_noise": noise_values["speed"],
            "status_mask": status_mask,
        }

        records.append(record)

    return records


def save_dataset(records):
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)


def verify_dataset():
    with OUTPUT_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        records = list(reader)

    timestamps_valid = True
    for record in records:
        try:
            parsed = datetime.fromisoformat(record["timestamp"])
            if parsed.tzinfo is None:
                timestamps_valid = False
        except (ValueError, TypeError):
            timestamps_valid = False

    no_missing_values = all(
        value not in (None, "") 
        for record in records
        for value in record.values()
    )

    sensor_ids_present = all(
        record["sensor_id"] == "UAV_SENSOR_SUITE_001"
        for record in records
    )

    phase_labels_valid = all(
        record["flight_phase"] in {"ascent", "cruise", "descent"}
        for record in records
    )

    print("\n--- Dataset Verification ---")
    print("Record count:", len(records))
    print("Expected columns:", columns == FIELDNAMES)
    print("No missing fields:", no_missing_values)
    print("Sensor IDs valid:", sensor_ids_present)
    print("Timestamps valid:", timestamps_valid)
    print("Flight phases valid:", phase_labels_valid)
    print("Output file:", OUTPUT_FILE)

    if records:
        print("\nFirst record:")
        print(records[0])

    if len(records) != TOTAL_RECORDS:
        raise ValueError("Unexpected number of generated records.")
    if columns != FIELDNAMES or not no_missing_values:
        raise ValueError("CSV structure verification failed.")
    if not timestamps_valid or not phase_labels_valid:
        raise ValueError("Timestamp or flight-phase verification failed.")


def main():
    records = generate_dataset()
    save_dataset(records)

    print("Synthetic UAV telemetry generation completed.")
    print("Records generated:", len(records))
    print("Noise models: Gaussian, correlated drift, bounded disturbance")

    verify_dataset()


if __name__ == "__main__":
    main()
