# Day 8 — ETL Pipeline Assembly (Pipeline v1)

## 1. Task Overview

**Task Name:** ETL Pipeline Assembly  
**Day:** 8  
**Date:** 12 October 2026  
**Project:** RUDRAEDGE RE-T1 (Spectra)  
**Role:** Software and Data Engineering  
**Pipeline Version:** v1  
**Execution Status:** Successfully Executed

## 2. Objective

The main objective of Day 8 was to develop and execute a standalone ETL (Extract, Transform, Load) pipeline for synthetic sensor telemetry data.

The pipeline was designed to perform the complete data-handling workflow, starting with dataset generation and continuing through extraction, validation, processing, and storage. The purpose was to understand how raw sensor readings can be organized into a structured dataset, checked for basic data-quality issues, processed into a consistent format, and stored for further analysis.

This task was implemented independently inside the Day8 directory. It does not depend on the Day7 Python script or Day7 dataset.

## 3. Practical Scope

The practical implementation covered the following stages:

1. Generate a new synthetic sensor dataset.
2. Extract the generated dataset using Pandas.
3. Validate records and identify basic data-quality problems.
4. Separate accepted records from rejected records.
5. Process valid records and calculate an additional time-based field.
6. Store processed data, rejected data, and a JSON summary.
7. Record pipeline execution information in a log file.

The pipeline demonstrates a basic data-engineering workflow in which each stage has a defined responsibility.

## 4. What Is ETL?

ETL stands for Extract, Transform, and Load.

### Extract
Extract means reading data from a source such as a CSV file, database, sensor log, or API. In this task, the generated CSV file was read into a Pandas DataFrame.

### Transform
Transform means checking, cleaning, converting, sorting, and preparing data for further use. In this pipeline, validation checks were performed, invalid records were separated, data types were standardized, and elapsed time was calculated for accepted records.

### Load
Load means saving the prepared data to a destination. In this implementation, accepted records, rejected records, and execution statistics were saved as output files.

### Dataset Generation
Before extraction, the pipeline generates its own synthetic dataset. This additional stage makes Day8 independent and ensures that the task does not require a pre-existing Day7 dataset.

## 5. Dataset Design

The pipeline generates 250 synthetic records using Python and Pandas. The data represents illustrative sensor readings associated with three flight phases: ascent, cruise, and descent.

The dataset contains the following columns:

| Column | Description |
|---|---|
| `record_id` | Identifier assigned to each record |
| `timestamp` | Time associated with a record, represented in UTC |
| `sensor_id` | Identifier of the simulated sensor |
| `flight_phase` | Simulated ascent, cruise, or descent phase |
| `temperature_c` | Temperature reading in degrees Celsius |
| `pressure_hpa` | Pressure reading in hectopascals |
| `altitude_m` | Altitude reading in meters |
| `speed_mps` | Speed reading in meters per second |
| `battery_v` | Simulated battery voltage in volts |

The dataset uses reproducible random values so that the same initial dataset can be generated again when the generator code and random seed remain unchanged.

The values are synthetic and intended only for software development and testing. They are not actual aircraft telemetry or certified operational measurements.

## 6. Stage 1 — Generate

The `generate_dataset()` function creates a new dataset independently within the Day8 pipeline.

It creates timestamps at regular five-second intervals and assigns sensor identifiers to the records. Flight phases are assigned using the record position: the first 80 records represent ascent, the next 100 represent cruise, and the remaining 70 represent descent.

The generator also creates simulated temperature, pressure, altitude, speed, and battery-voltage readings with small variations.

A few deliberate data-quality issues are introduced to demonstrate the validation stage. These include a missing temperature, an invalid timestamp, a negative speed, an unknown flight phase, a blank sensor identifier, a non-finite altitude, and a duplicated record identifier.

The generated dataset is saved as:

`synthetic_sensor_dataset.csv`

This file acts as the source dataset for the rest of the pipeline.

## 7. Stage 2 — Extract

The extraction stage reads the generated CSV file using Pandas.

The `extract_data()` function loads the source file into a DataFrame. A DataFrame provides a structured, table-like representation of the data and allows the pipeline to inspect columns, convert data types, filter rows, and perform calculations.

The extraction stage makes the generated records available to the validation function.

**Input:** `synthetic_sensor_dataset.csv`  
**Operation:** Read the CSV file into a Pandas DataFrame  
**Result:** 250 source records loaded

## 8. Stage 3 — Validate

Validation checks whether records satisfy the basic data-quality rules defined in the script.

The pipeline first checks whether all required columns are present. It then checks timestamps, record identifiers, sensor identifiers, flight phases, and numeric values.

### Validation rules

- Required columns must exist.
- Timestamps must be parseable as dates and times.
- Record identifiers must not be missing or duplicated.
- Sensor identifiers must not be blank.
- Flight phase must be one of the expected values: ascent, cruise, or descent.
- Numeric readings must be convertible to numeric values.
- Infinite numeric values are rejected.
- Speed must not be negative.
- Battery voltage and pressure must be greater than zero.
- Altitude must not be negative.

The script records rejection reasons so that invalid records can be inspected later. A record can have more than one rejection reason.

The validation stage produces two groups:

**Accepted records:** Records that pass the implemented checks.

**Rejected records:** Records that fail one or more implemented checks, with a `rejection_reason` field explaining the failure.

These rules are basic demonstration checks. They do not represent a complete aviation validation standard.

## 9. Stage 4 — Process

After validation, the `process_data()` function prepares the accepted records for storage and later analysis.

The processing stage performs these operations:

1. Converts timestamps into a consistent UTC datetime representation.
2. Converts record identifiers into integer values.
3. Converts sensor measurements into numeric floating-point values.
4. Sorts the accepted records by timestamp and record identifier.
5. Calculates `elapsed_seconds` relative to the earliest accepted timestamp.
6. Adds a `quality_status` column containing the value `accepted`.

The `elapsed_seconds` field helps express the time difference between a record and the beginning of the accepted dataset. This is useful for time-based analysis and plotting.

The processed dataset is saved as:

`processed_telemetry.csv`

## 10. Stage 5 — Store

The storage stage writes the pipeline results into files inside the same `Day8/codes` directory as the Python script.

### Output files

| File | Purpose |
|---|---|
| `synthetic_sensor_dataset.csv` | Original synthetic source dataset |
| `processed_telemetry.csv` | Accepted and processed records |
| `rejected_telemetry.csv` | Rejected records with reasons |
| `pipeline_summary.json` | Summary of execution and record counts |
| `etl_pipeline.log` | Timestamped execution log |

The JSON summary contains the pipeline version, execution status, source record count, accepted record count, rejected record count, runtime, flight-phase counts, output filenames, and a note explaining that the data is synthetic.

Keeping accepted and rejected records separate helps preserve information about data-quality failures instead of silently discarding invalid rows.

## 11. Tools and Libraries Used

### Python
Python was used to organize the pipeline into functions and execute the stages in sequence.

### Pandas
Pandas was used to create and manipulate tabular data, read and write CSV files, convert data types, filter records, sort rows, and calculate elapsed time.

### pathlib
The `pathlib` module was used to define file paths relative to the location of the script. This keeps the pipeline independent of a hard-coded Windows folder path.

### json
The `json` module was used to save the execution summary in a structured JSON format.

### logging
The `logging` module was configured to record timestamped pipeline messages in the log file.

### random
The `random` module was used to produce reproducible variations in synthetic sensor readings.

### datetime
The `datetime` module was used to create timestamps and represent them in UTC.

## 12. Actual Execution Results

The following values were observed in the terminal after running `python etl_pipeline.py`.

| Metric | Actual result |
|---|---:|
| Generated records | 250 |
| Accepted records | 242 |
| Rejected records | 8 |
| Runtime reported by the script | 1.276 seconds |
| Pipeline version | v1 |
| Output location | `Day8/codes/` |

The accepted-record percentage was calculated as:

242 / 250 × 100 = 96.8%

The rejected-record percentage was calculated as:

8 / 250 × 100 = 3.2%

These percentages describe the results of this particular execution. They do not measure the general accuracy or safety of a real sensor system.

## 13. Result Analysis

The pipeline successfully generated 250 records, loaded the generated dataset, separated records according to the implemented validation rules, processed 242 accepted records, and stored the output files.

Eight records were rejected. The rejected dataset preserves the associated rejection reasons so that the records can be examined instead of being removed without explanation.

The execution demonstrates the integration of data generation, extraction, validation, transformation, and storage in one Python workflow.

The reported runtime of 1.276 seconds is the value printed by the script during this run. It is specific to the current machine, software environment, dataset size, and execution conditions.

## 14. Limitations

- The dataset is synthetic rather than collected from physical sensors.
- Validation rules cover basic data-quality conditions only.
- The pipeline does not connect to a live sensor, aircraft, or database.
- The current implementation stores data in CSV and JSON files.
- The output does not establish the accuracy of real sensor measurements.
- No aviation safety or operational certification is claimed.

## 15. Possible Future Improvements

The pipeline can be extended by adding schema validation, configurable thresholds, stronger type checks, unit tests, automated data-quality reports, larger test datasets, database storage, and more detailed error handling.

Additional improvements could include a command-line configuration system, versioned output folders, and automated checks to confirm that saved files contain the expected number of records.

These are possible future improvements and are not claimed as completed features of Pipeline v1.

## 16. Conclusion

Day8 — ETL Pipeline Assembly (Pipeline v1) was implemented as a standalone data-engineering task.

The pipeline generated its own synthetic dataset and completed the generation, extraction, validation, processing, and storage stages. The observed execution produced 250 source records, of which 242 were accepted and processed and 8 were rejected.

The output files provide a structured basis for inspecting processed data, investigating rejected records, and reviewing execution statistics.

The task provided practical experience with Python, Pandas, CSV handling, data validation, transformation, JSON reporting, and execution logging.
