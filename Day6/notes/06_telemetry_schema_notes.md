
# Day 6 – Telemetry Schema Design

## 1. Introduction

Telemetry is the process of collecting and recording information from sensors or electronic systems. Sensor data may include temperature, pressure, altitude, speed, and other measurements.

In a multi-sensor system, different sensors can produce data in different formats. If the data does not follow a consistent structure, it becomes difficult to process, validate, store, and analyze it.

Telemetry Schema Design solves this problem by defining a standard format for telemetry records. It specifies the fields that each record should contain, the data type of each field, and whether a field is mandatory.

For the RUDRAEDGE RE-T1 project, this task focuses on designing a JSON-based telemetry schema that can be used by offline data-processing routines.

## 2. Task Information

- Task Name: Telemetry Schema Design
- Day: 6
- Date: 10 October 2026
- Role Context: Software & Data Engineer
- Main Objective: Design a consistent telemetry record structure.
- Required Output: Telemetry Schema

## 3. Objectives

The main objectives of this task are:

1. Define a standard structure for sensor telemetry records.
2. Identify required fields such as timestamps and sensor IDs.
3. Assign suitable data types to sensor measurements.
4. Define status-mask bits for representing record conditions.
5. Create a sample telemetry record in JSON format.
6. Develop a Python validator to check records against the schema.
7. Test both valid and invalid telemetry records.
8. Produce clear documentation for future integration with data-processing tasks.

## 4. Practical Scope

The practical implementation includes schema definition, sample-data creation, and basic validation.

The schema defines the expected structure. The sample JSON file demonstrates how a telemetry record should look. The Python validation script checks whether the record contains required fields and whether its values use the expected data types.

An invalid sample is also created by removing the required sensor ID field. This helps demonstrate how the validation script detects an incomplete record.

This implementation is a basic schema-validation routine. It does not yet implement every possible sensor boundary rule or verify the physical accuracy of sensor measurements.

## 5. Understanding the Telemetry Schema

A schema works like a blueprint for data.

For example, a telemetry record may contain:
- Timestamp
- Sensor ID
- Temperature
- Pressure
- Altitude
- Speed
- Status Mask

Each field has a defined purpose and data type.

A timestamp is represented as a string, measurements are represented as numbers, and the status mask is represented as an integer.

By using the same structure for every record, later processing routines can read telemetry consistently.

## 6. Schema Field Definitions

### 6.1 Timestamp

The timestamp records when a telemetry record was generated or associated with a measurement.

Example:
"timestamp": "2026-10-10T10:30:00Z"

The example uses an ISO-8601-style timestamp. The Z indicates Coordinated Universal Time (UTC).

A consistent timestamp format helps organize records chronologically and supports time-based analysis.

### 6.2 Sensor ID

The sensor ID identifies the source of the telemetry record.

Example:
"sensor_id": "SENSOR_001"

In a multi-sensor system, sensor IDs help distinguish records produced by different sources.

The ID is represented as a string because it is an identifier, not a numeric measurement.

### 6.3 Temperature

The temperature field stores a temperature measurement.

Example:
"temperature": 24.6

The selected unit is degrees Celsius (degC). A numeric data type allows the value to be processed mathematically.

### 6.4 Pressure

The pressure field stores a pressure measurement.

Example:
"pressure": 1013.2

The selected unit is hectopascals (hPa).

A consistent unit is important because values expressed in different pressure units cannot be compared directly without conversion.

### 6.5 Altitude

The altitude field stores an altitude measurement.

Example:
"altitude": 1500.0

The selected unit is meters (m).

The reference used to determine altitude, such as sea level or another reference point, should be specified by the system when required.

### 6.6 Speed

The speed field stores a speed measurement.

Example:
"speed": 12.5

The selected unit is meters per second (m/s).

Using a consistent unit makes it easier to compare records and perform calculations.

### 6.7 Status Mask

The status mask is an integer used to represent multiple status flags in a compact form.

Each bit represents a separate condition. A bit is either set (1) or clear (0).

The schema defines these four bits:

- Bit 0: Record structure valid
- Bit 1: Sensor data available
- Bit 2: Sensor reading within configured limits
- Bit 3: Timestamp valid

For example, the integer 15 has the binary representation 1111. All four defined bits are set.

However, setting a bit does not independently prove that its condition is true. The application must check the relevant condition before setting that bit.

In the current sample, 15 is a demonstration value used to represent all four flags as set.

## 7. Understanding the JSON Format

JSON stands for JavaScript Object Notation. It is a text-based format for representing structured data.

JSON supports common value types such as:
- String: text enclosed in quotation marks
- Number: an integer or decimal number
- Boolean: true or false
- Object: a collection of key-value pairs
- Array: an ordered collection of values
- Null: represents an absent or empty value

In this task, JSON is used for both the schema definition and the sample telemetry record.

Its readable structure makes it convenient to inspect, exchange, and process data using Python.

## 8. Project File Structure

The Day 6 implementation is organized as follows:

Day6/
    codes/
        telemetry_schema.json
        sample_telemetry.json
        invalid_sample.json
        validate_schema.py
        test_invalid_telemetry.py
    notes/
        06_telemetry_schema_notes.md
    logs/

### File Descriptions

**telemetry_schema.json**

Defines the schema name, schema version, expected fields, data types, required-field rules, and status-mask bit definitions.

**sample_telemetry.json**

Contains a sample record that follows the expected field structure.

**invalid_sample.json**

Contains a test record created by removing the required sensor_id field.

**validate_schema.py**

Loads the schema and checks the valid and invalid sample records.

**test_invalid_telemetry.py**

Creates an invalid sample record by removing the sensor_id field from the original sample.

**06_telemetry_schema_notes.md**

Documents the objective, design, implementation, testing, and outcome of the task.

## 9. Sample Telemetry Record

The sample record is:

{
  "timestamp": "2026-10-10T10:30:00Z",
  "sensor_id": "SENSOR_001",
  "temperature": 24.6,
  "pressure": 1013.2,
  "altitude": 1500.0,
  "speed": 12.5,
  "status_mask": 15
}

This example contains all the required fields defined by the schema.

The measurement values are illustrative sample data. They are not actual measurements from a physical sensor or a live system.

## 10. Python Validation Implementation

Python is used to load the JSON files and examine the telemetry records.

The validation routine performs the following checks:

### 10.1 Loading the Schema

The script reads telemetry_schema.json using Python's json module.

This provides access to the schema fields and their definitions.

### 10.2 Loading Telemetry Records

The script loads each sample JSON file and converts its contents into Python objects.

The record can then be examined field by field.

### 10.3 Required-Field Validation

The validator checks whether each required field is present.

For example, sensor_id is mandatory. If it is missing, the validator adds an error message.

### 10.4 Data-Type Validation

The validator checks whether each value uses its expected type.

For example:
- timestamp must be a string.
- sensor_id must be a string.
- temperature must be a number.
- status_mask must be an integer.

The implementation also prevents Boolean values from being accepted as ordinary numbers or integers.

### 10.5 Timestamp Validation

The validator checks whether the timestamp can be parsed and whether it includes a timezone.

This helps detect malformed or ambiguous timestamps.

### 10.6 Status-Mask Validation

The current implementation checks that status_mask is an integer between 0 and 15.

This range accommodates the four defined status bits.

The check validates the mask's numeric range; it does not verify that the underlying sensor conditions are actually true.

### 10.7 Reporting Results

If no errors are detected, the script displays:

VALIDATION: PASSED

If errors are detected, the script displays:

VALIDATION: FAILED

It also prints the corresponding error messages.

## 11. Testing Procedure

Two records are used to test the validation routine.

### Test Case 1: Valid Telemetry Record

Input: sample_telemetry.json

The record contains the required fields, expected data types, a parseable timestamp with a timezone, and a status mask within the configured range.

Expected Result:
VALIDATION: PASSED

Observed Result:
VALIDATION: PASSED

### Test Case 2: Missing Sensor ID

Input: invalid_sample.json

The record is created by removing sensor_id from the original sample.

Expected Result:
VALIDATION: FAILED

Observed Result:
VALIDATION: FAILED

The validator reports:

Missing required field: sensor_id

These results demonstrate that the script can distinguish the tested valid record from the tested incomplete record.

## 12. Tools and Technologies Used

### Python

Used to load JSON files, inspect field values, check data types, validate timestamps, and report errors.

### JSON

Used to represent the schema definition and telemetry records in a readable structured format.

### VS Code

Used to create, edit, organize, and execute the project files.

### Python Standard Library

- json: reads and writes JSON data.
- pathlib: manages file paths.
- datetime: parses timestamps and checks timezone information.

These libraries support the current implementation without requiring additional third-party packages.

## 13. Relationship to Data Processing

A consistent schema provides a foundation for later data-processing tasks.

For example:
1. A telemetry record is generated or received.
2. The record is checked against the expected structure.
3. Valid records can be passed to later processing stages.
4. Invalid records can be flagged for investigation.
5. Structured records can later be organized into tables for analysis.

This task establishes the record format and a basic validation mechanism. It does not by itself implement a complete telemetry ingestion or ETL pipeline.

## 14. Limitations and Future Improvements

The current implementation provides basic structural validation. Several improvements are possible:

- Add numerical boundary limits for temperature, pressure, altitude, and speed.
- Validate sensor IDs against a registered sensor list.
- Check whether timestamps are within an acceptable time range.
- Detect duplicate records and repeated timestamps where relevant.
- Define how missing or unavailable measurements should be represented.
- Set status-mask bits programmatically after checking each condition.
- Use a formal JSON Schema validator for more extensive schema rules.
- Add structured logging and summary reports for larger datasets.

These improvements can be implemented as separate tasks without changing the purpose of the basic schema.

## 15. Outcome

The telemetry schema was designed using JSON, with fields for timestamps, sensor identification, measurements, and status flags.

A sample record was created, and a Python script was implemented to validate required fields, data types, timestamp formatting, and status-mask range.

Testing showed that the valid sample passed and the incomplete sample failed with the expected missing-field message.

## 16. Conclusion

Telemetry Schema Design establishes a consistent format for storing and processing sensor records.

By defining field names, data types, required fields, and status-mask meanings, the task makes telemetry data easier to inspect and validate.

The completed implementation provides a starting point for future data-processing, telemetry validation, and pipeline integration work.
