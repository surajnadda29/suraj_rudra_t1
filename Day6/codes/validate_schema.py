
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
SCHEMA_FILE = BASE_DIR / "telemetry_schema.json"


def validate_record(record, schema):
    errors = []

    for field, rules in schema["fields"].items():
        if rules.get("required") and field not in record:
            errors.append(f"Missing required field: {field}")
            continue

        if field not in record:
            continue

        value = record[field]
        expected_type = rules["type"]

        if expected_type == "string" and not isinstance(value, str):
            errors.append(f"{field} must be a string")

        elif expected_type == "number" and (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            errors.append(f"{field} must be a number")

        elif expected_type == "integer" and (
            isinstance(value, bool) or not isinstance(value, int)
        ):
            errors.append(f"{field} must be an integer")

        elif expected_type == "number" and isinstance(value, (int, float)):
            if isinstance(value, float) and not __import__("math").isfinite(value):
                errors.append(f"{field} must be a finite number")

    timestamp = record.get("timestamp")

    if isinstance(timestamp, str):
        try:
            parsed = datetime.fromisoformat(
                timestamp.replace("Z", "+00:00")
            )
            if parsed.tzinfo is None:
                errors.append("timestamp must include a timezone")
        except ValueError:
            errors.append("timestamp must be valid ISO-8601")

    status_mask = record.get("status_mask")
    if isinstance(status_mask, int) and not isinstance(status_mask, bool):
        if not 0 <= status_mask <= 15:
            errors.append("status_mask must be between 0 and 15")

    return errors


def main():
    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        schema = json.load(file)

    test_files = [
        ("Valid sample", BASE_DIR / "sample_telemetry.json"),
        ("Invalid sample", BASE_DIR / "invalid_sample.json"),
    ]

    for label, file_path in test_files:
        print(f"\n--- {label} ---")

        if not file_path.exists():
            print("SKIPPED: File not found:", file_path.name)
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                record = json.load(file)
        except (json.JSONDecodeError, OSError) as error:
            print("FAILED: Could not read JSON:", error)
            continue

        errors = validate_record(record, schema)

        if errors:
            print("VALIDATION: FAILED")
            for error in errors:
                print("-", error)
        else:
            print("VALIDATION: PASSED")


if __name__ == "__main__":
    main()
