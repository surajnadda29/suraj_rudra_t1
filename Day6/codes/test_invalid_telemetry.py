
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
VALIDATOR = BASE_DIR / "validate_schema.py"
SAMPLE = BASE_DIR / "sample_telemetry.json"

# Load the original sample record
with open(SAMPLE, "r", encoding="utf-8") as file:
    record = json.load(file)

# Create an invalid record by removing sensor_id
record.pop("sensor_id", None)

# Save it temporarily
temp_file = BASE_DIR / "invalid_sample.json"
with open(temp_file, "w", encoding="utf-8") as file:
    json.dump(record, file, indent=2)

print("Test record created.")
print("Missing field: sensor_id")
print("Invalid record saved at:", temp_file)
print("Now check whether the validator detects this missing field.")
