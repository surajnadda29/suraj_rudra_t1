# Day 7 --- Synthetic UAV Flight Telemetry Generation with Realistic Noise Models

**Date:** 11 October 2026\
**Project:** RUDRAEDGE RE-T1 (Spectra)\
**Role:** Software & Data Engineer\
**Assigned Task:** Synthetic UAV Flight Telemetry Generation with
Realistic Noise Models\
**Expected Output:** Synthetic Dataset

------------------------------------------------------------------------

## 1. Introduction

Telemetry records measurements from sensors or devices for later storage
and processing. In a UAV context, telemetry may include timestamps,
temperature, pressure, altitude, and speed. Synthetic telemetry is
artificially generated data that follows a defined structure and is
useful when real hardware readings are unavailable.

For this task, a Python program was developed to generate a time-ordered
dataset representing simplified UAV flight phases. The dataset is for
software testing and learning only. It is not collected from a real UAV
and does not represent validated flight dynamics, operational limits, or
certified sensor behavior.

## 2. Objective

The objective was to create a reusable generator that produces 1,000
synthetic telemetry records at one-second intervals, simulates ascent,
cruise, and descent phases, adds multiple noise components, saves the
data as CSV, and verifies the saved output.

The expected output is a synthetic dataset suitable for offline
data-processing and testing activities.

## 3. Program Architecture

The program follows this sequence:

1.  Configure the record count, output path, sample interval, random
    seed, and CSV columns.
2.  Generate a UTC timestamp for each record.
3.  Select an illustrative flight phase based on the record's position
    in the sequence.
4.  Calculate baseline temperature, pressure, altitude, and speed
    values.
5.  Add the configured noise components to the baselines.
6.  Save the records in CSV format.
7.  Read the saved file back and verify its structure and selected
    fields.

The code separates generation, saving, and verification into functions
so the workflow is easier to maintain.

## 4. Tools and Libraries Used

-   **Python:** Generates the records and runs verification.
-   **`csv`:** `DictWriter` writes the records; `DictReader` reads them
    back.
-   **`random`:** Generates Gaussian noise, drift increments, and
    occasional disturbances.
-   **`math`:** `sin()` creates smooth cruise-phase variation; `exp()`
    is used in the simplified pressure baseline.
-   **`datetime`:** Generates UTC timestamps and one-second time
    increments.
-   **`pathlib`:** Creates an output path relative to the Python script.
-   **Visual Studio Code and PowerShell:** Used to edit, run, and
    inspect the program.

`random.seed(42)` makes the pseudorandom sequence repeatable under the
same code and conditions. The complete CSV still differs across runs
because its starting timestamp uses the current UTC time.

## 5. Configuration

-   `TOTAL_RECORDS = 1000`: generates 1,000 data rows, excluding the
    header.
-   `SAMPLE_INTERVAL_SECONDS = 1`: advances each timestamp by one
    second.
-   `random.seed(42)`: initializes the pseudorandom sequence.
-   `OUTPUT_FILE`: saves the result as
    `synthetic_uav_flight_telemetry.csv` in the script's directory.
-   `FIELDNAMES`: defines the twelve CSV columns and their order.

## 6. Dataset Schema

  Field                 Purpose
  --------------------- -----------------------------------------------
  `timestamp`           UTC timestamp for the sample
  `sensor_id`           Demonstration sensor-suite identifier
  `flight_phase`        `ascent`, `cruise`, or `descent`
  `temperature`         Simulated temperature measurement
  `pressure`            Simulated pressure measurement
  `altitude`            Simulated altitude measurement
  `speed`               Simulated speed measurement
  `temperature_noise`   Combined simulated noise added to temperature
  `pressure_noise`      Combined simulated noise added to pressure
  `altitude_noise`      Combined simulated noise added to altitude
  `speed_noise`         Combined simulated noise added to speed
  `status_mask`         Fixed demonstration status value

The noise columns allow the simulated deviations to be examined
separately. One sensor-suite identifier is used for all rows; the
current version does not model independent packets from separate
physical sensors. Units are not stored as separate metadata fields.

## 7. Timestamp and Sampling Strategy

The generator uses the current UTC time as its starting timestamp and
removes microseconds. For each record, it adds the record index
multiplied by the one-second sample interval. Therefore, consecutive
records are scheduled one second apart.

This is a simulated sampling schedule. It does not model actual hardware
clock accuracy, communication delays, timestamp jitter, or
synchronization behavior.

## 8. Simulated Flight Phases

The data is divided into three illustrative phases based on progress
through the record sequence.

### Ascent

The first 35% of records are labelled `ascent`. Baseline altitude
increases from approximately 100 to 500, while baseline speed increases
from approximately 35 to 50.

### Cruise

The next 40% of records are labelled `cruise`. Baseline altitude remains
near 500 and speed remains near 50, with small smooth sinusoidal
variations.

### Descent

The final 25% of records are labelled `descent`. Baseline altitude
decreases from approximately 500 to 100, while baseline speed decreases
from approximately 50 to 38.

These are demonstration values. Units are not explicitly represented and
the patterns are not a validated UAV flight or aerodynamic model.

## 9. Baseline Measurements

The generator uses the following simplified baselines:

-   Temperature: `25 - 0.006 * base_altitude`
-   Pressure: `1013.25 * exp(-base_altitude / 8434.5)`
-   Altitude and speed: values determined by the selected flight phase.

These equations create a changing time-series dataset. They do not
include a validated atmosphere model, calibrated environmental
conditions, or operational sensor specifications.

## 10. Noise Models Implemented

The generator combines three types of simulated variation.

### 10.1 Gaussian Measurement Noise

`random.gauss(0, scale)` generates random errors around zero. The
configured scales are 0.25 for temperature, 0.80 for pressure, 1.20 for
altitude, and 0.45 for speed. This is a simplified measurement-noise
model; actual sensor errors may follow different distributions.

### 10.2 Correlated Sensor Drift

Each measurement has a drift state that retains part of its previous
value and adds a new random increment. This creates gradual variation
across adjacent samples rather than fully independent noise. It is
useful for testing software with slowly changing measurement bias, but
the parameters are illustrative and have not been calibrated using real
sensor data.

### 10.3 Occasional Bounded Disturbances

For each measurement, the program has a 2% chance of adding a small
disturbance bounded by twice that measurement's Gaussian-noise scale in
either direction. This adds occasional deviations for testing while
limiting their magnitude. It is not a model of a specific real-world
vibration, impact, or fault.

### 10.4 Combined Noise

The total noise is the sum of Gaussian noise, the current drift state,
and any disturbance. The combined value is stored in the corresponding
`*_noise` field and added to the baseline measurement. Noise values are
rounded to four decimal places; measurements are rounded to three
decimal places.

## 11. Status Mask

The program assigns `status_mask = 15` to every record. In binary, 15 is
`1111`, meaning its lowest four bits are set. In the previous Day 6
demonstration schema, these bits represented record structure validity,
sensor data availability, readings within configured demonstration
limits, and timestamp validity.

Day 7 does not independently calculate these conditions; it assigns the
value directly. Therefore, a value of 15 is only a demonstration value
and does not prove that a record passed sensor-health or
operational-limit checks.

## 12. CSV Generation

The output file is:

`Day7/codes/synthetic_uav_flight_telemetry.csv`

The program uses UTF-8 encoding and `csv.DictWriter` to write the header
and each record. The file contains a header row followed by 1,000
telemetry records. It can be opened in a spreadsheet application or
loaded into Python tools such as Pandas for further offline analysis.

The previous file `synthetic_telemetry.csv` is not the output filename
used by the updated generator.

## 13. Verification and Test Results

The `verify_dataset()` function reads the saved CSV and checks:

1.  The number of records equals the configured 1,000.
2.  The CSV header matches all twelve expected columns in the correct
    order.
3.  No loaded field is empty.
4.  Every row has the expected sensor-suite ID.
5.  Each timestamp parses successfully and contains timezone
    information.
6.  Each flight-phase label is one of `ascent`, `cruise`, or `descent`.

The user ran the updated script and confirmed that the output file was
created and the verification checks printed `True`.

These checks confirm basic structure and consistency, not physical
accuracy or full statistical quality. The verifier does not currently
check every numeric value for finiteness, validate measurement limits,
or prove that the noise distribution matches real sensors.

## 14. Execution Procedure

The Python file is saved as:

`Day7/codes/synthetic_telemetry_generator.py`

Run it from the `Day7/codes` directory:

``` powershell
python synthetic_telemetry_generator.py
```

The script generates the CSV, prints the record count and noise models,
and runs the verification checks. The generated dataset is saved as
`synthetic_uav_flight_telemetry.csv`.

## 15. Relationship to Previous and Future Tasks

Day 6 focused on defining a telemetry schema and checking required
fields and data types. Day 7 builds on that structure by producing a
time-series dataset with simulated flight phases and multiple noise
components.

The CSV can be used in later Pandas processing, data validation, and ETL
exercises. Downstream scripts must account for the updated twelve-column
schema, including `flight_phase` and the four noise fields.

## 16. Limitations

-   Flight phases and baselines are simplified illustrative patterns,
    not validated UAV dynamics.
-   Measurement units are not stored as metadata.
-   Noise parameters are examples and are not calibrated against real
    sensors.
-   One sensor-suite ID is used for all records.
-   The status mask is fixed at 15 and is not computed from validation
    results.
-   Verification checks basic structure but not complete numeric,
    physical, or statistical validity.
-   The random seed is fixed, but the starting UTC timestamp changes
    between runs.
-   A `clamp()` helper is defined in the code but is not currently used.

The dataset should be used for software testing and learning, not as
real UAV telemetry or as a validated flight simulation.

## 17. Possible Future Improvements

Future versions could add explicit units and schema-version metadata,
configurable start times, more comprehensive numeric and statistical
checks, status-mask calculation from validation results, optional
missing or out-of-range values for fault testing, configurable record
counts, and summary reports.

These are proposed improvements, not features implemented in the current
version.

## 18. Output Files and Folder Structure

``` text
Day7/
├── codes/
│   ├── synthetic_telemetry_generator.py
│   └── synthetic_uav_flight_telemetry.csv
├── notes/
│   └── 07_synthetic_telemetry_notes.md
└── logs/
    └── Daily diary for 11 October 2026
```

The Python script contains the generation logic, the CSV contains the
synthetic dataset, the notes explain the design and limitations, and the
logs folder is reserved for the daily diary.

## 19. Final Outcome

A Python-based synthetic UAV flight telemetry generator was implemented
and run successfully. It generated 1,000 time-ordered records with
illustrative ascent, cruise, and descent phases. The dataset contains
temperature, pressure, altitude, and speed values with Gaussian
measurement noise, correlated drift, and occasional bounded
disturbances.

The data was saved as `synthetic_uav_flight_telemetry.csv`. The user
confirmed that the output file was created and the implemented
verification checks passed. This provides a structured synthetic dataset
for subsequent offline telemetry processing and software testing, while
remaining clearly identified as demonstration data rather than real UAV
telemetry.
