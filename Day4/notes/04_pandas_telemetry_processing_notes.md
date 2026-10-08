# Day 4 – Pandas Telemetry Processing

## Date
07 October 2026

## Task
Pandas Telemetry Processing

## Required Output
Pandas-based telemetry processing and validation with processed CSV output.

---

# 1. Introduction

The main focus of Day 4 was to use Pandas for processing, analyzing, validating, and exporting telemetry data.

In this project, telemetry data refers to numerical data that can be obtained from different sensors or system monitoring sources. In this task, the telemetry dataset was processed using a Pandas DataFrame.

The following operations were performed during this task:

- Handling telemetry data using a Pandas DataFrame
- Converting timestamps into datetime format
- Setting the timestamp as the DataFrame index
- Performing time-based data selection
- Filtering data based on temperature
- Sorting telemetry data
- Generating statistical summaries
- Checking for missing values
- Checking for duplicate records
- Validating sensor values against defined ranges
- Exporting processed telemetry data to a CSV file
- Performing final dataset verification

This task is directly related to my **Software & Data Engineer** role because offline telemetry processing, data validation, and data auditing are important responsibilities of this role.

---

# 2. Task Objective

The objective of Day 4 was to use Pandas to process telemetry data in a structured and systematic way.

The main objectives were:

1. Manage telemetry data using a DataFrame.
2. Convert timestamps into the proper datetime format.
3. Select records based on a specific time range.
4. Filter records according to specific conditions.
5. Sort the data according to a required parameter.
6. Obtain statistical information from the dataset.
7. Identify missing values.
8. Identify duplicate records.
9. Check sensor values against defined validation ranges.
10. Save the processed data as a CSV file.
11. Verify the final processed output.

---

# 3. My Project Role

My project role is:

**Software & Data Engineer**

My role mainly focuses on offline data processing, telemetry handling, synthetic data processing, data validation, and data auditing.

For Day 4, Pandas was used to process and validate telemetry data.

The focus of this task was not flight control, hardware control, or direct sensor hardware programming. The focus was on the software side of telemetry data processing, organization, validation, analysis, and export.

---

# 4. Tools and Technologies Used

The following tools and technologies were used for the Day 4 task:

- Python
- Pandas
- Jupyter Notebook
- VS Code
- Python Virtual Environment
- CSV file format

## Pandas

Pandas is an important Python data-processing library used for handling and analyzing structured data.

## Jupyter Notebook

Jupyter Notebook was used to execute the code cell by cell and immediately observe the output.

## VS Code

VS Code was used to manage the project folder, virtual environment, and Jupyter Notebook.

## CSV

The processed telemetry data was exported as a CSV file for storage and future use.

---

# 5. Python Virtual Environment

A Python virtual environment was used inside the project.

A virtual environment is an isolated Python environment in which the packages required for a particular project can be installed separately.

The main benefit is that packages installed for one project do not interfere with the environment of another project.

For Day 4, Pandas was installed inside the project environment.

The following command was used to install Pandas:

```bash
python -m pip install pandas
```

After installation, Pandas was imported into the Python notebook.

---

# 6. Importing Pandas

Pandas was imported into the Python program using:

```python
import pandas as pd
```

Here, `pd` is the commonly used short name or alias for Pandas.

After importing Pandas, its functions and methods can be accessed using `pd`.

Example:

```python
pd.DataFrame()
```

---

# 7. What is Telemetry Data?

Telemetry data is data that represents the operating condition or measurements of a system.

In this project task, the telemetry dataset contained numerical parameters such as:

- Temperature
- Pressure
- Altitude
- Speed
- Timestamp

These values are useful for system monitoring, offline analysis, validation, and reporting.

Example:

| Timestamp | Temperature | Pressure | Altitude | Speed |
|---|---:|---:|---:|---:|
| 09:00 | 25.0 | 1012 | 120 | 45 |
| 09:01 | 26.1 | 1011 | 125 | 47 |
| 09:02 | 27.3 | 1010 | 130 | 50 |
| 09:03 | 28.0 | 1009 | 135 | 52 |
| 09:04 | 27.6 | 1011 | 132 | 49 |

This example represents how telemetry records can be organized.

---

# 8. What is a DataFrame?

A **DataFrame** is a two-dimensional tabular data structure provided by Pandas.

A DataFrame can be understood as a table containing:

- Rows = individual records
- Columns = variables or parameters

For example:

```text
Temperature   Pressure   Altitude   Speed
------------------------------------------
25.0          1012       120        45
26.1          1011       125        47
27.3          1010       130        50
```

Each row represents one telemetry record.

---

# 9. Rows and Columns

In the telemetry DataFrame, rows represent individual telemetry records.

Columns represent different telemetry parameters.

The final processed DataFrame contained the following columns:

```text
temperature
pressure
altitude
speed
```

The timestamp was used as the DataFrame index.

The final DataFrame shape was:

```text
(5, 4)
```

This means:

- 5 records/rows
- 4 data columns

---

# 10. Timestamp in Telemetry Data

A timestamp is very important in telemetry data.

It indicates the exact date and time at which a particular telemetry value was recorded.

For example:

```text
2026-08-10 09:01:00
```

This contains:

- Date = 10 August 2026
- Time = 09:01:00

Time information is useful for telemetry analysis because specific time periods can be selected and analyzed.

---

# 11. Converting Timestamp into Datetime

Initially, the timestamp was not in the required datetime format.

For time-based operations, the timestamp was converted into Pandas datetime format.

Code:

```python
telemetry_df["timestamp"] = pd.to_datetime(telemetry_df["timestamp"])
```

The `pd.to_datetime()` function converts timestamp values into a proper datetime format.

This allows Pandas to understand the timestamp as date and time information.

---

# 12. Why Datetime Conversion Was Required

Datetime conversion was required because time-based selection works properly when the timestamp is stored in a datetime-compatible format.

After conversion, Pandas can:

- Understand dates
- Understand time values
- Select specific time ranges
- Perform date-based filtering
- Perform time-series operations

Therefore, converting the timestamp into datetime format was an important step in telemetry processing.

---

# 13. Creating DatetimeIndex

After converting the timestamp into datetime format, it was set as the DataFrame index.

Code:

```python
telemetry_df = telemetry_df.set_index("timestamp")
```

The timestamp was no longer treated as a normal data column.

It became the DataFrame index.

The structure was approximately:

```text
Timestamp              Temperature  Pressure  Altitude  Speed
----------------------------------------------------------------
2026-08-10 09:00:00    25.0         1012      120       45
2026-08-10 09:01:00    26.1         1011      125       47
2026-08-10 09:02:00    27.3         1010      130       50
2026-08-10 09:03:00    28.0         1009      135       52
2026-08-10 09:04:00    27.6         1011      132       49
```

---

# 14. Why DatetimeIndex is Important

A DatetimeIndex is useful for telemetry data because records can be accessed directly according to their timestamps.

For example:

```python
telemetry_df.loc[
    "2026-08-10 09:01:00":"2026-08-10 09:03:00"
]
```

This selects the records between 09:01 and 09:03.

Without a proper DatetimeIndex, this type of time-based selection does not work as expected.

---

# 15. Time-Based Telemetry Selection

The `.loc[]` method was used to select telemetry records within a specific time range.

Code:

```python
time_range_data = telemetry_df.loc[
    "2026-08-10 09:01:00":"2026-08-10 09:03:00"
]
```

This code selects the records between the specified start and end timestamps.

Time-based selection is useful because it allows us to:

- Analyze a specific time interval
- Examine data related to a particular event
- Extract a required period from a large telemetry dataset
- Perform focused offline analysis

---

# 16. Problem Faced During Time-Based Selection

During the time-based selection, the expected output was initially not obtained.

The DataFrame index was initially:

```text
RangeIndex(start=0, stop=5, step=1)
```

This indicated that the timestamp was not being used as a datetime index.

Therefore, when the time-range query was performed, the expected records were not returned.

The problem was solved using:

```python
telemetry_df["timestamp"] = pd.to_datetime(
    telemetry_df["timestamp"]
)

telemetry_df = telemetry_df.set_index(
    "timestamp"
)
```

After this, the DataFrame had a `DatetimeIndex`, and time-based selection worked successfully.

---

# 17. Filtering Telemetry Data

Filtering means selecting required records based on a specific condition.

During Day 4, telemetry records were filtered based on temperature.

Code:

```python
filtered_data = telemetry_df[
    telemetry_df["temperature"] > 27
]
```

This means that only records where the temperature was greater than 27 were selected.

---

# 18. Boolean Condition

Pandas filtering works using Boolean conditions.

Example:

```python
telemetry_df["temperature"] > 27
```

This condition checks every row.

The result can internally be represented as:

```text
True
False
True
False
True
```

Rows where the condition is `True` are included in the filtered DataFrame.

---

# 19. Why Filtering is Important

Telemetry datasets can become very large.

If thousands or millions of records are available, manually identifying required records becomes difficult.

Filtering allows us to quickly identify:

- High-temperature records
- Low-pressure records
- High-altitude records
- High-speed records
- Records matching specific conditions

Therefore, filtering is important for both telemetry analysis and data validation.

---

# 20. Sorting Telemetry Data

Sorting means arranging data according to a particular column or parameter.

The telemetry data was sorted according to temperature in descending order.

Code:

```python
sorted_data = telemetry_df.sort_values(
    by="temperature",
    ascending=False
)
```

Here:

- `by="temperature"` means sorting according to temperature.
- `ascending=False` means sorting from the highest value to the lowest value.

---

# 21. Why Sorting is Useful

Sorting is useful when analyzing telemetry data.

For example, if we want to identify the highest temperature records, descending sorting makes this easier.

Similarly, sorting can be used to identify:

- Highest speed
- Highest altitude
- Lowest pressure
- Highest temperature

This makes data analysis more convenient.

---

# 22. Statistical Analysis

A statistical summary was generated to analyze the telemetry dataset.

Code:

```python
summary = telemetry_df[
    ["temperature", "pressure", "altitude", "speed"]
].describe()

summary
```

The `describe()` function provides a statistical summary of numerical columns.

---

# 23. `describe()` Function

The `describe()` function generally provides the following information:

### Count

The number of valid numerical records.

### Mean

The average value of the data.

### Standard Deviation

Shows how much the values are spread around the mean.

### Minimum

The smallest value in the column.

### 25%

The first quartile.

### 50%

The median value.

### 75%

The third quartile.

### Maximum

The largest value in the column.

This summary helps in quickly understanding the overall statistical behavior of the telemetry dataset.

---

# 24. Missing Value Validation

Telemetry datasets may contain missing values.

A missing value means that an expected value is not available for a particular record.

Missing values were checked using:

```python
missing_values = telemetry_df.isnull().sum()

missing_values
```

---

# 25. Understanding `isnull().sum()`

The following code:

```python
telemetry_df.isnull().sum()
```

performs two main operations.

### `isnull()`

Checks whether each value is missing.

### `sum()`

Counts the total number of missing values in each column.

For example:

```text
temperature    0
pressure       0
altitude       0
speed          0
```

means that there are no missing values in the respective columns.

---

# 26. Why Missing Values Matter

Missing values can affect telemetry data analysis.

For example, if a temperature value is missing and an average is calculated, the analysis may be affected.

Missing values can cause:

- Changes in statistical calculations
- Incomplete filtering
- Inaccurate reports
- Problems in further data processing
- Potential issues in machine learning workflows

Therefore, checking for missing values is an important data validation step.

---

# 27. Duplicate Record Validation

Telemetry data may also contain duplicate records.

A duplicate record means that the same record appears more than once.

Duplicate records were checked using:

```python
duplicate_count = telemetry_df.duplicated().sum()

duplicate_count
```

Final result:

```text
Duplicate records: 0
```

This means that no duplicate records were found in the dataset.

---

# 28. Why Duplicate Checking is Important

Duplicate telemetry records can affect data analysis.

If the same record appears multiple times:

- The record count may become incorrect.
- Statistical results may be affected.
- Average values may change.
- Reports may become inaccurate.

Therefore, duplicate validation is an important data auditing step.

---

# 29. Temperature Range Validation

Temperature values were checked against a defined validation range.

Code:

```python
temperature_check = telemetry_df[
    (telemetry_df["temperature"] < 20) |
    (telemetry_df["temperature"] > 40)
]

temperature_check
```

This condition means:

- If temperature is below 20
- OR temperature is above 40

then the record is displayed as an out-of-range record.

The result was an empty DataFrame.

This means:

**No temperature value was found outside the defined validation range.**

Important:

These values were used as practical validation limits for this task. They should not be considered actual UAV operating limits.

---

# 30. Pressure Range Validation

Pressure values were checked against a defined validation range.

Code:

```python
pressure_check = telemetry_df[
    (telemetry_df["pressure"] < 950) |
    (telemetry_df["pressure"] > 1050)
]

pressure_check
```

If the pressure is:

- Below 950
- OR above 1050

the record is displayed as an out-of-range record.

The result was an empty DataFrame.

This means:

**No pressure value was found outside the defined validation range.**

---

# 31. Altitude Range Validation

Altitude was validated using:

```python
altitude_check = telemetry_df[
    (telemetry_df["altitude"] < 0) |
    (telemetry_df["altitude"] > 500)
]

altitude_check
```

The condition checks whether:

- Altitude is below 0
- OR altitude is above 500

The result was an empty DataFrame.

This means:

**No altitude value was found outside the defined validation range.**

---

# 32. Speed Range Validation

Speed was validated using:

```python
speed_check = telemetry_df[
    (telemetry_df["speed"] < 0) |
    (telemetry_df["speed"] > 200)
]

speed_check
```

The condition checks whether:

- Speed is below 0
- OR speed is above 200

The result was an empty DataFrame.

This means:

**No speed value was found outside the defined validation range.**

---

# 33. Meaning of Empty DataFrame During Validation

An output such as:

```text
Empty DataFrame
```

does not always mean that there is an error.

In this task, it means that no record satisfied the specified invalid condition.

For example:

```python
temperature_check
```

returned an empty DataFrame.

This means:

```text
No temperature values were outside the defined validation range.
```

The same result was obtained for pressure, altitude, and speed validation.

Therefore, the validation checks were successful.

---

# 34. Data Auditing

Data auditing means systematically checking data to identify missing, incorrect, duplicate, or unusual records.

The following auditing checks were performed during Day 4:

- Missing value check
- Duplicate record check
- Temperature range check
- Pressure range check
- Altitude range check
- Speed range check

These checks help ensure that the processed telemetry dataset satisfies the basic validation requirements.

---

# 35. Exporting Processed Telemetry Data

After processing and validation, the telemetry data was exported to a CSV file.

Code:

```python
telemetry_df.to_csv("processed_telemetry.csv")

print("Processed telemetry data saved successfully.")
```

This created the file:

```text
processed_telemetry.csv
```

---

# 36. What is CSV?

CSV stands for:

**Comma-Separated Values**

CSV is a simple tabular data format used to store structured data.

Example:

```text
timestamp,temperature,pressure,altitude,speed
2026-08-10 09:00:00,25.0,1012,120,45
2026-08-10 09:01:00,26.1,1011,125,47
```

CSV files can be easily used with:

- Python
- Pandas
- Excel
- Database tools
- Data analysis software

---

# 37. Why CSV Output was Created

The processed data was saved as a CSV file so that the final telemetry dataset could be reused for future analysis or reporting.

CSV output is:

- Portable
- Easy to read
- Easy to load using Pandas
- Compatible with many tools
- Convenient for data sharing

---

# 38. Final Dataset Verification

After completing the processing, the final dataset was verified.

Code:

```python
print("Total records:", len(telemetry_df))
print("Columns:", list(telemetry_df.columns))
print("Data shape:", telemetry_df.shape)
print("Missing values:", telemetry_df.isnull().sum().sum())
print("Duplicate records:", telemetry_df.duplicated().sum())
```

Final output:

```text
Total records: 5
Columns: ['temperature', 'pressure', 'altitude', 'speed']
Data shape: (5, 4)
Missing values: 0
Duplicate records: 0
```

---

# 39. Understanding Final Output

## Total Records

```text
5
```

This means that the DataFrame contains a total of 5 telemetry records.

## Columns

```text
['temperature', 'pressure', 'altitude', 'speed']
```

This means that four numerical telemetry parameters are present.

The timestamp is used as the DataFrame index.

## Data Shape

```text
(5, 4)
```

This means:

```text
5 rows × 4 columns
```

## Missing Values

```text
0
```

This means that there are no missing values in the final dataset.

## Duplicate Records

```text
0
```

This means that no duplicate records were found.

---

# 40. Complete Day 4 Workflow

The complete Day 4 workflow was:

```text
Telemetry Data
      ↓
Pandas DataFrame
      ↓
Timestamp Conversion
      ↓
DatetimeIndex
      ↓
Time-Based Selection
      ↓
Data Filtering
      ↓
Data Sorting
      ↓
Statistical Analysis
      ↓
Missing Value Check
      ↓
Duplicate Check
      ↓
Range Validation
      ↓
Processed Telemetry Data
      ↓
CSV Export
      ↓
Final Verification
```

---

# 41. Problems Faced During the Task

## Problem 1 – Pandas Environment

Initially, Pandas had to be installed in the project environment.

### Solution

Pandas was installed using:

```bash
python -m pip install pandas
```

After that:

```python
import pandas as pd
```

was successfully executed.

---

## Problem 2 – Python Shell Confusion

The Python interpreter displayed:

```text
>>>
```

This indicated that the Python interactive shell was running.

The Python shell was exited using:

```python
exit()
```

After that, the normal PowerShell/terminal prompt was available again.

---

## Problem 3 – Time Range Query Returned No Expected Data

The time-range selection initially did not provide the expected output.

The reason was that the DataFrame index was:

```text
RangeIndex
```

instead of a datetime index.

### Solution

The timestamp was converted and assigned as the index:

```python
telemetry_df["timestamp"] = pd.to_datetime(
    telemetry_df["timestamp"]
)

telemetry_df = telemetry_df.set_index(
    "timestamp"
)
```

After this, time-based selection worked successfully.

---

# 42. Data Processing Concepts Learned

Through Day 4, I practically learned the following concepts:

## Pandas DataFrame

Handling structured data in a tabular form.

## Datetime

Converting timestamps into a proper date-time format.

## DatetimeIndex

Using timestamps as a DataFrame index for time-based analysis.

## Filtering

Selecting records according to a condition.

## Sorting

Arranging data according to a specific column.

## Statistical Analysis

Obtaining count, mean, standard deviation, minimum, maximum, and quartile information.

## Missing Value Detection

Identifying incomplete records.

## Duplicate Detection

Identifying repeated records.

## Range Validation

Checking sensor values against defined validation ranges.

## CSV Export

Saving processed data in a reusable file format.

---

# 43. Relation With Software & Data Engineer Role

The Day 4 task is directly connected to my Software & Data Engineer role.

Important areas of my role include:

- Offline data processing
- Telemetry processing
- Data validation
- Data auditing
- Data organization
- Reporting

During Day 4, these concepts were practically implemented using Pandas.

Telemetry data was organized into a DataFrame.

The timestamp was processed to perform time-based data selection.

Filtering and sorting were used for data analysis.

A statistical summary was generated to understand the dataset.

Missing values and duplicate records were checked.

Sensor parameters were validated against defined ranges.

Finally, the processed dataset was exported as a CSV file.

---

# 44. Why Pandas is Useful for My Role

As a Software & Data Engineer, telemetry datasets can potentially become very large.

Manually processing large datasets can be difficult and time-consuming.

Pandas provides functions for:

- Data loading
- Data cleaning
- Data filtering
- Data sorting
- Data aggregation
- Missing value handling
- Duplicate detection
- Time-series processing
- Data export

Therefore, Pandas is a useful tool for offline telemetry processing.

---

# 45. Difference Between Data Processing and Data Validation

## Data Processing

Data processing means organizing, transforming, and analyzing the data.

Examples:

- Timestamp conversion
- Filtering
- Sorting
- DataFrame creation
- Statistical analysis

## Data Validation

Data validation means checking whether the data satisfies expected conditions.

Examples:

- Missing value check
- Duplicate check
- Temperature range check
- Pressure range check
- Altitude range check
- Speed range check

Both data processing and data validation were performed during Day 4.

---

# 46. Final Result

At the end of Day 4, the telemetry data was successfully processed and validated.

Final verification:

```text
Total records: 5
Columns: ['temperature', 'pressure', 'altitude', 'speed']
Data shape: (5, 4)
Missing values: 0
Duplicate records: 0
```

Range validation also produced successful results:

- Temperature: No out-of-range records
- Pressure: No out-of-range records
- Altitude: No out-of-range records
- Speed: No out-of-range records

The processed data was exported to:

```text
processed_telemetry.csv
```

---

# 47. Task Outcome

The Day 4 task was successfully completed.

Main outcomes:

- Pandas environment was successfully configured.
- Telemetry data was processed using a DataFrame.
- Timestamp was converted into datetime format.
- A DatetimeIndex was created.
- Time-based telemetry selection was performed.
- Temperature-based filtering was performed.
- Data was sorted according to temperature.
- Statistical summary was generated.
- Missing values were validated.
- Duplicate records were validated.
- Sensor parameter ranges were validated.
- Processed data was exported in CSV format.
- Final dataset verification was completed.

---

# 48. Interview Explanation

If the interviewer asks:

## "What did you do in Day 4?"

I can explain:

> My Day 4 task was Pandas Telemetry Processing. I used Python and Pandas to process a telemetry dataset containing timestamp, temperature, pressure, altitude, and speed values. I converted the timestamp into datetime format and created a DatetimeIndex so that I could perform time-based data selection. After that, I performed filtering, sorting, and statistical analysis using Pandas. I also validated the dataset for missing values, duplicate records, and out-of-range sensor values. Finally, I exported the processed telemetry data into a CSV file and verified the final dataset.

---

# 49. Short Interview Version

If the interviewer asks for a short answer:

> Day 4 involved using Pandas to process telemetry data. I performed datetime conversion, time-based selection, filtering, sorting, statistical analysis, missing-value checking, duplicate checking, and sensor range validation. Finally, I exported the processed data to a CSV file.

---

# 50. Important Pandas Functions Used

The important Pandas functions and methods used during Day 4 were:

## Import Pandas

```python
import pandas as pd
```

## Convert Timestamp

```python
pd.to_datetime()
```

Used for timestamp conversion.

## Set Index

```python
DataFrame.set_index()
```

Used to set the timestamp as the DataFrame index.

## Time-Based Selection

```python
DataFrame.loc[]
```

Used for time-based record selection.

## Filtering

```python
DataFrame[]
```

Used for filtering records according to conditions.

## Sorting

```python
DataFrame.sort_values()
```

Used for sorting data.

## Statistical Summary

```python
DataFrame.describe()
```

Used for generating statistical summaries.

## Missing Values

```python
DataFrame.isnull()
```

Used for detecting missing values.

## Duplicate Records

```python
DataFrame.duplicated()
```

Used for detecting duplicate records.

## CSV Export

```python
DataFrame.to_csv()
```

Used for exporting processed data to CSV.

## Data Shape

```python
DataFrame.shape
```

Used for checking the number of rows and columns.

## Total Records

```python
len(DataFrame)
```

Used for counting the total number of records.

---

# 51. Important Concepts to Remember

The following points are especially important for Day 4:

1. **Pandas** is a Python library used for structured data processing.
2. **DataFrame** is Pandas' tabular data structure.
3. **Timestamp** represents the date and time of a telemetry record.
4. `pd.to_datetime()` converts timestamps into datetime format.
5. `set_index("timestamp")` sets the timestamp as the DataFrame index.
6. **DatetimeIndex** is important for time-based data selection.
7. `.loc[]` can be used for label-based and time-based selection.
8. Boolean conditions are used for filtering.
9. `sort_values()` is used for sorting data.
10. `describe()` provides a statistical summary of numerical data.
11. `isnull().sum()` is useful for counting missing values.
12. `duplicated().sum()` is useful for counting duplicate records.
13. Range validation helps identify unusual or out-of-range values.
14. An empty validation result can mean that no invalid records were found.
15. `to_csv()` saves processed data to a CSV file.
16. Final verification is important for confirming data quality.

---

# 52. Conclusion

During Day 4, I practically used Pandas to perform a complete telemetry data processing and validation workflow.

The task involved more than simply reading the data. The telemetry data was structured into a DataFrame, processed, analyzed, and validated.

The timestamp was converted into datetime format and used as a DatetimeIndex. Time-based selection was then performed to extract records from a specific time interval.

The telemetry values were also filtered and sorted for analysis. A statistical summary was generated to understand the numerical characteristics of the dataset.

Data quality checks were performed for missing values and duplicate records. Temperature, pressure, altitude, and speed were also checked against defined validation ranges.

Finally, the processed telemetry dataset was exported to a CSV file and the final dataset was verified.

This task provided practical experience relevant to my **Software & Data Engineer** role, particularly in offline telemetry processing, data validation, data auditing, structured data handling, and reporting.