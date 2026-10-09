# Day 5 — Data Validation & Error Checks

**Project:** RUDRAEDGE RE-T1 (Spectra)  
**Role:** Software & Data Engineer  
**Task Date:** 9 October 2026  
**Implementation Language:** Python  
**Primary Library:** Pandas

---

## 1. Introduction

Telemetry is the process of collecting and transmitting data from sensors or electronic systems to another system for monitoring, analysis, and processing.

In a sensor-based system, telemetry records may contain temperature, pressure, altitude, speed, timestamps, and packet identifiers. These values are useful only when they are sufficiently complete, correctly formatted, and consistent with the validation rules defined for the system.

During data transmission or processing, records may contain missing values, incorrect data types, invalid timestamps, duplicate packet identifiers, or sensor readings outside acceptable ranges.

Data validation is the process of checking these records against predefined rules before they are accepted for further processing.

In this task, a Python validation script was developed to examine simulated telemetry records, identify common data-quality issues, separate valid and rejected records, and generate CSV outputs containing the validation results.

## 2. Objective

The primary objective of this task is to implement a basic telemetry validation system that can identify common data-quality problems.

The specific objectives are:

1. Validate required telemetry fields.
2. Identify missing sensor readings.
3. Check sensor readings against defined boundary limits.
4. Detect invalid timestamp values.
5. Identify duplicate packet identifiers.
6. Detect incorrect numeric data types.
7. Flag timestamps that are earlier than the preceding record.
8. Separate valid and rejected records.
9. Record rejection reasons for troubleshooting.
10. Generate CSV files containing validated data and validation results.

These checks demonstrate the basic principles of telemetry data validation. They do not, by themselves, certify the safety or reliability of an aircraft or any other physical system.

## 3. Practical Scope

The practical scope defines the activities covered by this implementation.

### 3.1 Telemetry Data Ingestion

The script starts with a simulated dataset containing telemetry fields. The data is stored in a Python list of dictionaries and converted into a Pandas DataFrame.

Each dictionary represents one telemetry record.

The dataset includes:

- `timestamp` — the time associated with a record.
- `packet_id` — an identifier used to track a telemetry packet.
- `temperature` — a simulated temperature reading.
- `pressure` — a simulated pressure reading.
- `altitude` — a simulated altitude reading.
- `speed` — a simulated speed reading.

Using simulated data makes it possible to test validation rules without relying on actual flight telemetry.

### 3.2 Data-Quality Checks

The script checks whether required fields are present and whether values can be interpreted in the expected format.

For example, a missing temperature reading or a speed value containing the text `unknown` should not be treated as a valid numeric measurement.

### 3.3 Boundary Validation

Numeric readings are compared against configured minimum and maximum values.

A reading outside the configured range is flagged as a boundary violation. The limits in this exercise are demonstration values and must not be interpreted as certified operating limits.

### 3.4 Packet and Timestamp Checks

The script identifies repeated packet IDs, invalid timestamps, and records whose timestamps are earlier than the preceding record.

These checks help demonstrate how a telemetry processing pipeline can identify suspicious records before further analysis.

### 3.5 Output Generation

After applying the checks, the script produces separate outputs for valid records, rejected records, and a summary report.

The rejection reasons help explain why a particular record failed validation.

## 4. Tools and Libraries Used

### 4.1 Python

Python is the programming language used to implement the validation logic.

It supports conditional statements, loops, functions, data structures, and file operations needed to process telemetry records.

### 4.2 Pandas

Pandas is used to represent the telemetry data as a DataFrame and perform data-quality checks.

Important Pandas operations used in this practical include:

- `pd.DataFrame()` — converts a list of dictionaries into a table.
- `isna()` — identifies missing values.
- `pd.to_numeric()` — attempts to convert values into numeric form.
- `pd.to_datetime()` — parses timestamps into datetime values.
- `duplicated()` — identifies repeated values in selected columns.
- `loc[]` — selects records using conditions.
- `to_csv()` — exports a DataFrame to a CSV file.

### 4.3 Visual Studio Code

Visual Studio Code is used to create and edit the Python script, organize the project folders, and inspect the generated files.

### 4.4 PowerShell Terminal

The terminal is used to execute the Python script and inspect the CSV output files.

Commands such as `python`, `Get-Content`, and `Import-Csv` help verify that the script runs and that the outputs contain the expected information.

## 5. Sample Telemetry Dataset

The sample dataset contains seven records with six fields.

| Field | Purpose | Example |
|---|---|---|
| `timestamp` | Identifies the recorded time | `2026-10-09 10:00:00` |
| `packet_id` | Identifies a packet | `PKT001` |
| `temperature` | Stores a temperature reading | `28.5` |
| `pressure` | Stores a pressure reading | `1005.2` |
| `altitude` | Stores an altitude reading | `120.0` |
| `speed` | Stores a speed reading | `45.0` |

The dataset contains deliberately introduced test cases, including a missing temperature, an out-of-range pressure value, an invalid timestamp, a repeated packet ID, an invalid speed value, and an out-of-order timestamp.

These cases are designed to verify whether the validation rules can identify the expected problems.

## 6. Detailed Validation Rules

### 6.1 Required-Column Validation

A telemetry dataset must contain the columns required by the processing pipeline.

For this exercise, the required columns are:

`timestamp`, `packet_id`, `temperature`, `pressure`, `altitude`, and `speed`.

If a required column is absent, the script raises a `ValueError` explaining which columns are missing.

**Why is this important?**

If a column is missing, subsequent validation logic may fail or produce incomplete results. Checking the dataset structure early makes the problem easier to diagnose.

**Current limitation:** This check verifies that required columns exist. It does not validate every aspect of a packet's original binary structure or communication protocol.

### 6.2 Missing-Value Validation

A missing value means that an expected field does not contain a usable measurement.

For example:

| Packet ID | Temperature |
|---|---:|
| PKT001 | 28.5 |
| PKT002 | Missing |

The second record does not provide a temperature measurement.

The script uses `isna()` to identify missing values. During numeric conversion, values that cannot be converted may also become missing numeric values.

**Why is this important?**

Missing sensor readings can affect calculations, statistical summaries, and downstream data-processing operations. They should be identified before the record is used.

In this implementation, records with missing or invalid required numeric readings are rejected rather than silently filled with invented values.

### 6.3 Numeric Data-Type Validation

Sensor readings are expected to be numeric.

Examples of numeric values include:

- `28.5`
- `1005.2`
- `120`
- `45.0`

A value such as `unknown` is text and cannot be interpreted as a numeric speed reading.

The script uses:

`pd.to_numeric(column, errors="coerce")`

The `errors="coerce"` option converts values that cannot be parsed into missing numeric values. The validation logic then identifies those values as invalid.

**Why is this important?**

Numeric validation prevents text or malformed values from being mistakenly used in mathematical operations or sensor-range comparisons.

A production system should also distinguish between a genuinely missing value and a nonnumeric value so that the rejection reason remains precise.

### 6.4 Boundary-Limit Validation

Boundary validation checks whether a numeric reading lies within the configured minimum and maximum values.

The demonstration ranges used in this practical are:

| Field | Minimum | Maximum |
|---|---:|---:|
| Temperature | 20 | 40 |
| Pressure | 950 | 1050 |
| Altitude | 0 | 500 |
| Speed | 0 | 200 |

For a field with minimum \(L_{\min}\) and maximum \(L_{\max}\), the reading is within the configured range when:

\[
L_{\min} \leq x \leq L_{\max}
\]

A reading is outside the range when:

\[
x < L_{\min} \quad \text{or} \quad x > L_{\max}
\]

For example, a pressure reading of `1200.0` exceeds the demonstration maximum of `1050`. The script therefore flags packet `PKT003` for a pressure boundary violation.

**Why is this important?**

Boundary checks help identify implausible readings, sensor faults, configuration problems, and possible data-quality issues.

**Important limitation:** A boundary violation does not automatically prove that a sensor or packet is corrupted. Real thresholds must be based on verified sensor specifications, operating conditions, and system requirements. The ranges in this exercise are illustrative only.

### 6.5 Timestamp Validation

A timestamp indicates when a telemetry record is associated with a measurement.

A valid example is:

`2026-10-09 10:00:00`

An invalid example is:

`INVALID_TIME`

The script uses `pd.to_datetime()` with `errors="coerce"` to parse timestamp strings. A value that cannot be parsed becomes a missing datetime value and is flagged as invalid.

**Why is this important?**

Timestamps are used to organize records chronologically, compare measurements over time, and identify delayed or out-of-order records.

Invalid timestamps can interfere with time-based analysis and make it difficult to determine when a measurement was recorded.

### 6.6 Duplicate Packet-ID Detection

A packet ID is used to identify a telemetry packet.

The sample data contains two records with the packet ID `PKT002`.

The script uses Pandas duplicate detection with `keep="first"`. Under this rule, the first occurrence is retained and a subsequent occurrence is flagged as a duplicate.

**Why is this important?**

Duplicate packets may occur when data is retransmitted or when a processing system receives the same record more than once. Unhandled duplicates can inflate counts or distort statistical calculations.

**Current limitation:** The implementation assumes packet IDs should be unique within the dataset. A production system must define the uniqueness scope, such as a device ID combined with a sequence number or time window. Repeated IDs alone do not prove that the packet contents are corrupted.

### 6.7 Stale or Out-of-Order Timestamp Detection

A timestamp is out of order when it occurs earlier than the preceding record's timestamp in the dataset.

For example:

| Packet ID | Timestamp |
|---|---|
| PKT006 | 2026-10-09 10:00:05 |
| PKT007 | 2026-10-09 09:00:00 |

The second timestamp is earlier than the first, so the script flags `PKT007` as stale or out of order.

The implementation compares each parsed timestamp with the previous row's timestamp using `shift(1)`.

**Why is this important?**

Out-of-order records can complicate time-series processing and can indicate delayed delivery, reordering, or incorrect timestamps.

**Current limitation:** A timestamp earlier than the preceding row is not necessarily stale. The record may simply have arrived out of order. Reliable staleness detection requires an agreed time threshold and, ideally, a separate packet-arrival timestamp.

### 6.8 Missing Packet-ID Validation

The script checks whether `packet_id` is missing or contains only whitespace.

A missing packet ID makes it harder to trace, compare, or deduplicate a record reliably.

Such a record is flagged with a rejection reason.

### 6.9 Corrupted or Malformed Packet Detection

In this practical, corrupted or malformed telemetry is represented through detectable data-quality problems such as:

- Missing required columns
- Missing packet IDs
- Invalid timestamps
- Incorrect numeric values
- Missing sensor readings

These checks detect certain malformed records at the DataFrame level.

Actual communication-packet corruption requires protocol-specific validation. Depending on the format, that may include packet length checks, sequence numbers, checksums, or CRC verification.

Therefore, the current implementation is a basic telemetry-record validation exercise, not a complete communication-protocol integrity checker.

## 7. Validation and Rejection Logic

The script creates a copy of the input DataFrame and prepares a field named `error_reason`.

Each validation rule appends an explanatory message when a record fails a check.

For example:

`pressure outside demo limits;`

A record with no recorded validation errors is classified as valid. A record with one or more recorded errors is classified as rejected.

The intended classification is:

- **Valid:** No validation errors detected by the implemented rules.
- **Rejected:** At least one validation error detected.

This approach makes the output easier to review because the rejected record includes the reason it failed.

A production implementation should use structured error codes as well as readable descriptions, and should explicitly define whether certain errors result in rejection, warning, or manual review.

## 8. Output Files and Their Purpose

All generated CSV files are stored in `Day5/codes/`, according to the agreed project structure.

### 8.1 `telemetry_validation.py`

This is the main Python script. It contains the sample telemetry dataset, validation rules, record-classification logic, and CSV export operations.

### 8.2 `valid_telemetry.csv`

This file contains the records that passed the checks implemented in the script.

It can be used as the input for later data-processing stages, provided that the validation rules are appropriate for the intended application.

### 8.3 `rejected_telemetry.csv`

This file contains rejected records along with their `error_reason` values.

The observed output identified these six cases:

1. `PKT002` — Missing temperature.
2. `PKT003` — Pressure outside demonstration limits.
3. `PKT004` — Invalid timestamp.
4. `PKT002` — Duplicate packet ID.
5. `PKT006` — Invalid speed data type.
6. `PKT007` — Stale or out-of-order timestamp.

This demonstrates that the implemented checks identify the intended test cases.

### 8.4 `validation_report.csv`

This file summarizes the total, valid, and rejected record counts.

The report must be generated after the latest validation logic has run successfully. Its counts should be verified against the current output files rather than assumed.

If the script processes seven records and rejects six distinct records, the remaining record count is one. The final report should reflect the actual script output.

## 9. Project Folder Structure

The Day 5 folder follows this structure:

```text
Day5/
├── codes/
│   ├── telemetry_validation.py
│   ├── valid_telemetry.csv
│   ├── rejected_telemetry.csv
│   └── validation_report.csv
├── notes/
│   └── 05_data_validation_notes.md
└── logs/
    └── Day5_Diary_09-10-2026.docx
```

The `codes` folder contains the script and generated CSV outputs. The `notes` folder contains the technical explanation. The `logs` folder is reserved for the daily diary.

## 10. Testing and Verification

The script is executed from the `Day5` directory using:

```powershell
python .\codes\telemetry_validation.py
```

The rejected records are inspected using:

```powershell
Import-Csv .\codes\rejected_telemetry.csv |
Format-Table packet_id, error_reason -AutoSize
```

The validation report is inspected using:

```powershell
Get-Content .\codes\validation_report.csv
```

The observed rejected-record output contains six entries corresponding to the intentionally introduced test cases.

After each change to the validation logic, the script must be rerun so that the CSV files reflect the latest rules.

## 11. Limitations and Future Improvements

The current implementation demonstrates basic telemetry data-quality checks. It can be improved in the following ways:

1. **Structured error codes:** Store a stable code for each error in addition to its description.
2. **Separate missing and malformed values:** Distinguish a genuinely absent reading from a nonnumeric reading.
3. **Configurable thresholds:** Load verified sensor ranges from a configuration file.
4. **Stronger timestamp handling:** Define a staleness window and track packet-arrival time separately.
5. **Packet-integrity verification:** Add protocol-specific length, checksum, or CRC checks when the actual packet format is known.
6. **Improved duplicate handling:** Define uniqueness using device identifiers, packet sequence numbers, and the appropriate time window.
7. **Automated tests:** Add test cases for valid records, missing fields, boundary violations, duplicate IDs, and invalid timestamps.
8. **More detailed reporting:** Record counts by error category and include a run timestamp.
9. **Logging:** Use Python's logging module to record execution status and unexpected errors.
10. **Scalability:** Process large telemetry datasets in chunks or use more efficient validation strategies where required.

These improvements would make the validation system easier to maintain, test, and adapt to real telemetry requirements.

## 12. Conclusion

The Day 5 task demonstrated how Python and Pandas can be used to validate telemetry records and identify common data-quality problems.

The implementation covers required-field checks, missing values, numeric data types, boundary limits, timestamp parsing, duplicate packet IDs, and out-of-order timestamps. It separates valid and rejected records and records rejection reasons in a CSV output.

The practical establishes a foundation for future telemetry processing, auditing, and data-integrity work. Further protocol-specific checks and verified operational requirements would be necessary before applying the system to real safety-critical telemetry.

---
