import pandas as pd

# Sample telemetry data for validation testing
telemetry_data = [
    {
        "timestamp": "2026-10-09 10:00:00",
        "packet_id": "PKT001",
        "temperature": 28.5,
        "pressure": 1005.2,
        "altitude": 120.0,
        "speed": 45.0,
    },
    {
        "timestamp": "2026-10-09 10:00:01",
        "packet_id": "PKT002",
        "temperature": None,
        "pressure": 1004.8,
        "altitude": 125.0,
        "speed": 46.0,
    },
    {
        "timestamp": "2026-10-09 10:00:02",
        "packet_id": "PKT003",
        "temperature": 29.1,
        "pressure": 1200.0,
        "altitude": 130.0,
        "speed": 48.0,
    },
    {
        "timestamp": "INVALID_TIME",
        "packet_id": "PKT004",
        "temperature": 29.4,
        "pressure": 1003.5,
        "altitude": 135.0,
        "speed": 49.0,
    },
    {
        "timestamp": "2026-10-09 10:00:04",
        "packet_id": "PKT002",
        "temperature": 29.7,
        "pressure": 1002.9,
        "altitude": 140.0,
        "speed": 50.0,
    },
    {
        "timestamp": "2026-10-09 10:00:05",
        "packet_id": "PKT006",
        "temperature": 30.0,
        "pressure": 1002.5,
        "altitude": 145.0,
        "speed": "unknown",
    },
    {
        "timestamp": "2026-10-09 09:00:00",
        "packet_id": "PKT007",
        "temperature": 29.8,
        "pressure": 1001.8,
        "altitude": 150.0,
        "speed": 47.0,
    },
]

df = pd.DataFrame(telemetry_data)

print("Sample telemetry data:")
print(df.to_string(index=False))

print("\nTotal records:", len(df))
print("Total columns:", len(df.columns))

print("\n--- Basic Data Quality Checks ---")

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Check duplicate packet IDs
print("\nDuplicate packet IDs:")
print(df[df.duplicated(subset=["packet_id"], keep=False)])

print("\n--- Boundary Limit Checks ---")

# Demonstration limits only, not certified flight limits
limits = {
    "temperature": (20, 40),
    "pressure": (950, 1050),
    "altitude": (0, 500),
    "speed": (0, 200),
}

for column, (minimum, maximum) in limits.items():
    values = pd.to_numeric(df[column], errors="coerce")

    invalid = values.notna() & (
        (values < minimum) | (values > maximum)
    )

    print(f"\n{column.capitalize()} limit: {minimum} to {maximum}")
    print(df.loc[invalid, ["packet_id", column]])

    print("\n--- Corrupted Packet Detection ---")

# Detect invalid timestamps
parsed_time = pd.to_datetime(df["timestamp"], errors="coerce")
invalid_timestamps = parsed_time.isna()

print("\nInvalid timestamps:")
print(df.loc[invalid_timestamps, ["packet_id", "timestamp"]])

# Detect duplicate packet IDs
duplicate_packets = df.duplicated(
    subset=["packet_id"],
    keep="first"
)

print("\nDuplicate packets:")
print(df.loc[duplicate_packets, ["packet_id", "timestamp"]])

# Detect invalid numeric data types
numeric_columns = [
    "temperature",
    "pressure",
    "altitude",
    "speed"
]

for column in numeric_columns:
    converted = pd.to_numeric(df[column], errors="coerce")
    invalid_type = df[column].notna() & converted.isna()

    print(f"\nInvalid {column} values:")
    print(df.loc[invalid_type, ["packet_id", column]])

    print("\n--- Final Record Validation ---")

# Convert sensor columns to numeric values
numeric_columns = [
    "temperature",
    "pressure",
    "altitude",
    "speed"
]

clean_df = df.copy()

for column in numeric_columns:
    clean_df[column] = pd.to_numeric(
        clean_df[column], errors="coerce"
    )

# Validate timestamps
clean_df["timestamp"] = pd.to_datetime(
    clean_df["timestamp"], errors="coerce"
)

# Mark records with validation errors
clean_df["error_reason"] = ""

for column in numeric_columns:
    clean_df.loc[
        clean_df[column].isna(),
        "error_reason"
    ] += f"Invalid or missing {column}; "

# Check sensor boundaries
for column, (minimum, maximum) in limits.items():
    invalid = (
        clean_df[column].notna()
        & (
            (clean_df[column] < minimum)
            | (clean_df[column] > maximum)
        )
    )

    clean_df.loc[invalid, "error_reason"] += (
        f"{column} outside demo limits; "
    )

# Check timestamps
clean_df.loc[
    clean_df["timestamp"].isna(),
    "error_reason"
] += "Invalid timestamp; "

# Reject repeated packet IDs
duplicate = clean_df.duplicated(
    subset=["packet_id"], keep="first"
)

clean_df.loc[duplicate, "error_reason"] += (
    "Duplicate packet ID; "
)


# Flag timestamps that are older than the previous packet
previous_time = clean_df["timestamp"].shift(1)

stale_or_out_of_order = (
    clean_df["timestamp"].notna()
    & previous_time.notna()
    & (clean_df["timestamp"] < previous_time)
)

clean_df.loc[
    stale_or_out_of_order, "error_reason"
] += "Stale or out-of-order timestamp; "

# Check required packet fields
required_columns = [
    "timestamp",
    "packet_id",
    "temperature",
    "pressure",
    "altitude",
    "speed",
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Malformed telemetry dataset: missing columns {missing_columns}"
    )

# Check missing packet IDs
missing_packet_id = (
    df["packet_id"].isna()
    | df["packet_id"].astype(str).str.strip().eq("")
)

clean_df.loc[
    missing_packet_id, "error_reason"
] += "Missing packet ID; "


# Separate valid and rejected records
valid_records = clean_df[
    clean_df["error_reason"] == ""
].copy()

rejected_records = clean_df[
    clean_df["error_reason"] != ""
].copy()

print("Total records:", len(clean_df))
print("Valid records:", len(valid_records))
print("Rejected records:", len(rejected_records))

print("\nRejected record details:")
print(
    rejected_records[
        ["packet_id", "error_reason"]
    ].to_string(index=False)
)

print("\n--- Saving Validation Outputs ---")

# Save valid telemetry records
valid_records.to_csv(
    "codes/valid_telemetry.csv",
    index=False
)

# Save rejected records with error reasons
rejected_records.to_csv(
    "codes/rejected_telemetry.csv",
    index=False
)

# Create validation summary report
report = pd.DataFrame({
    "metric": [
        "Total Records",
        "Valid Records",
        "Rejected Records"
    ],
    "count": [
        len(clean_df),
        len(valid_records),
        len(rejected_records)
    ]
})

report.to_csv(
    "codes/validation_report.csv",
    index=False
)

print("Valid records saved.")
print("Rejected records saved.")
print("Validation report saved.")