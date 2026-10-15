# Day-11: Telemetry Fault Recovery

**Project:** RUDRAEDGE RE-T1 (Spectra)  
**Date:** 15 October 2026  
**Task:** Corrupted and Missing Telemetry Handling with Interpolation Logic

## 1. Introduction

Telemetry is the process of collecting and transferring sensor data for monitoring and analysis. In a UAV system, telemetry may contain temperature, pressure, altitude, and speed readings.

During data collection, some readings may be missing or corrupted. These errors can affect further calculations and data analysis. The purpose of this task is to detect invalid readings, handle missing values, and recover suitable values using interpolation.

## 2. Objectives

- Load the synthetic UAV telemetry dataset from Day-7 when available.
- Detect missing and out-of-range sensor readings.
- Replace invalid readings with missing values.
- Apply linear interpolation to suitable missing values.
- Save the recovered data and a summary of the results.

## 3. Tools and Libraries

- **Python:** Used to implement the recovery routine.
- **Pandas:** Used for CSV handling, data cleaning, missing-value detection, and interpolation.
- **NumPy:** Used for numerical operations and generating demonstration data if the previous dataset is unavailable.
- **Pathlib:** Used to manage file paths.
- **JSON:** Used to save the recovery summary.

## 4. Dataset Preparation

The program first searches for the Day-7 file named `synthetic_uav_flight_telemetry.csv`.

If the file is available in the expected location, it is loaded using Pandas. Otherwise, the program creates a synthetic demonstration dataset containing timestamp, sensor identifier, temperature, pressure, altitude, and speed.

The program creates a separate copy of the dataset and introduces a few controlled faults to test the recovery process, including missing readings, an unusually high temperature, and a negative speed value.

## 5. Fault Detection and Validation

The program checks sensor readings against illustrative ranges:

| Sensor | Minimum | Maximum |
|---|---:|---:|
| Temperature | -50 | 120 |
| Pressure | 100 | 1200 |
| Altitude | -500 | 10000 |
| Speed | 0 | 200 |

Values outside these ranges are identified as invalid and converted into missing values before recovery.

These limits are for demonstration only. Real UAV applications require appropriate sensor specifications and validated operating limits.

## 6. Linear Interpolation

Linear interpolation estimates a missing value using surrounding valid readings.

For example, if altitude readings are 100 m and 120 m, with one missing reading between them at equal time intervals, interpolation estimates the middle value as 110 m.

The program uses Pandas interpolation with `method="linear"` and `limit_area="inside"`. This fills suitable internal gaps while leaving missing values at the beginning or end unfilled.

Interpolated readings are estimates, not guaranteed original measurements.

## 7. Working Process

The program follows these steps:

1. Loads the previous dataset or creates demonstration data.
2. Prepares the timestamp and sensor columns.
3. Introduces controlled test faults.
4. Detects missing and out-of-range readings.
5. Converts invalid values into missing values.
6. Applies linear interpolation to suitable gaps.
7. Counts recovered and remaining missing values.
8. Saves the processed data and recovery summary.

## 8. Output Files

The program generates two output files inside the `codes` folder:

- **`recovered_telemetry.csv`** — contains the processed telemetry after validation and interpolation.
- **`recovery_summary.json`** — records the number of invalid readings, recovered readings, remaining missing values, and the ranges used for each sensor.

The terminal also displays a summary of the recovery process.

## 9. Limitations

- The demonstration data may be synthetic rather than actual UAV flight data.
- Sensor limits are illustrative and must be verified before real-world use.
- Interpolation estimates missing readings and may not reproduce the actual sensor values.
- Missing values at the edges may remain unresolved.

## 10. Conclusion

In this task, a telemetry fault recovery routine was implemented using Python, Pandas, and NumPy. The program checks sensor ranges, identifies invalid readings, handles missing values, and applies linear interpolation to suitable gaps.

The recovered telemetry and JSON summary provide a basic record of the processing results. This task establishes a foundation for further telemetry validation and data-processing work in the RUDRAEDGE RE-T1 (Spectra) project.
