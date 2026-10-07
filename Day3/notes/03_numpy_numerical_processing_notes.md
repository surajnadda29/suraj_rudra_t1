# RUDRAEDGE RE-T1 (Spectra)
## Day 3 — NumPy Numerical Processing & Vectorized Numerical Processing

**Date:** 07 October 2026  
**Engineer:** Suraj Nadda  
**Role:** Software & Data Engineer  
**Task:** NumPy Numerical Processing  
**Primary Output:** `NumPy_Numerical_Processing.ipynb`

---

# 1. Task Objective

The objective of Day 3 was to study and implement NumPy-based numerical processing techniques for offline telemetry and sensor-data processing.

NumPy was used to understand how numerical data can be stored, manipulated, analyzed, filtered, transformed, and processed efficiently using arrays.

The practical work focused mainly on:

- Creating NumPy arrays
- Working with 1D and 2D numerical data
- Accessing data using indexing and slicing
- Performing arithmetic operations
- Performing statistical calculations
- Filtering numerical data using conditions
- Understanding vectorized processing
- Comparing normal Python loops with NumPy vectorized operations
- Understanding broadcasting
- Generating synthetic telemetry data
- Performing telemetry validation
- Normalizing numerical telemetry data
- Building a basic numerical processing routine

The data used during this practical was synthetic and generated locally. No real operational or sensitive project data was used.

---

# 2. What is NumPy?

NumPy stands for **Numerical Python**.

It is a Python library designed mainly for numerical and scientific computing. Its most important feature is the **NumPy array**, which allows large amounts of numerical data to be stored and processed efficiently.

A normal Python list can also store numbers, but NumPy arrays provide specialized numerical operations that are more suitable for scientific and engineering applications.

For example, instead of processing every value individually using a Python loop, NumPy allows an operation to be applied directly to an entire array.

Example:

```python
data = np.array([10, 20, 30, 40, 50])

result = data * 2
```

The multiplication operation is applied to every element of the array.

Result:

```text
[20 40 60 80 100]
```

This type of operation is one of the foundations of vectorized numerical processing.

---

# 3. Why NumPy is Important for the RE-T1 Data Engineering Role

The Software & Data Engineer role involves offline data processing, telemetry handling, synthetic data generation, data validation and auditing.

Telemetry and sensor systems can produce large quantities of numerical data. Examples of numerical parameters can include:

- Temperature
- Pressure
- Voltage
- Altitude
- Speed
- Sensor measurements
- Time-series numerical readings

Such data needs to be processed before it can be analyzed or used by later stages of a data pipeline.

NumPy is useful because it provides efficient operations for:

- Numerical calculations
- Statistical analysis
- Array manipulation
- Filtering
- Transformation
- Normalization
- Synthetic data generation
- Numerical validation

Therefore, learning NumPy provides the numerical-processing foundation required before moving to Pandas-based telemetry processing.

---

# 4. NumPy Environment Setup

A separate virtual environment was created for Day 3 to keep the task environment isolated.

The Day 3 environment contains NumPy required for the numerical-processing practical.

The virtual environment was created using:

```powershell
python -m venv .venv
```

It was activated using:

```powershell
.\.venv\Scripts\Activate.ps1
```

NumPy was installed using:

```powershell
python -m pip install numpy
```

The installed NumPy version was also verified before starting the practical.

This approach keeps the Day 3 work reproducible and separates its dependencies from other tasks.

---

# 5. NumPy Import and Version Verification

The first step in the notebook was importing NumPy:

```python
import numpy as np
```

The name `np` is a commonly used short alias for NumPy.

The installed version was checked using:

```python
np.__version__
```

This confirms that NumPy is available inside the selected Python environment.

The initial verification is important because a numerical-processing notebook should use a known and working library environment.

---

# 6. One-Dimensional NumPy Array

A one-dimensional array was created using temperature readings:

```python
temperature = np.array([
    24.5, 25.1, 26.3, 27.0, 26.7, 25.9
])
```

This represents a simple sequence of numerical sensor readings.

The following properties were checked:

```python
temperature.shape
temperature.size
temperature.dtype
```

### Shape

`shape` describes the structure of the array.

For six values:

```text
(6,)
```

This means the array contains six elements in one dimension.

### Size

`size` gives the total number of elements.

```text
6
```

### Data Type

`dtype` specifies the type of numerical values stored in the array.

For decimal values, NumPy generally uses a floating-point data type.

---

# 7. Array Indexing

NumPy uses zero-based indexing.

For example:

```text
Index:        0     1     2     3     4     5
Value:       24.5  25.1  26.3  27.0  26.7  25.9
```

Therefore:

```python
temperature[0]
```

returns the first value.

```python
temperature[2]
```

returns the third value.

Negative indexing can also be used:

```python
temperature[-1]
```

returns the last value.

Indexing is useful when a particular sensor reading needs to be accessed.

---

# 8. Array Slicing

Slicing is used to extract a portion of an array.

Example:

```python
temperature[:3]
```

returns the first three readings.

Another example:

```python
temperature[-3:]
```

returns the last three readings.

Slicing is useful when only a specific portion of a telemetry sequence needs to be analyzed.

It avoids manually selecting every individual value.

---

# 9. NumPy Array Arithmetic

NumPy allows mathematical operations to be performed directly on arrays.

Example:

```python
increased_temp = temperature_c + 2
```

This adds `2` to every temperature value.

Another example:

```python
temperature_f = (temperature_c * 9/5) + 32
```

This converts the complete temperature array from Celsius to Fahrenheit.

Similarly:

```python
temperature_difference = temperature_c - 25
```

calculates the difference of every reading from the reference temperature of 25°C.

The important feature is that the operation is applied to the complete array without writing a separate loop for each value.

---

# 10. Statistical Operations

Numerical telemetry needs to be summarized and analyzed.

NumPy provides several built-in statistical functions.

The practical used:

```python
np.min()
np.max()
np.mean()
np.median()
np.std()
```

### Minimum

```python
np.min(temperature_c)
```

returns the smallest temperature value.

### Maximum

```python
np.max(temperature_c)
```

returns the largest value.

### Mean

```python
np.mean(temperature_c)
```

calculates the average value.

### Median

```python
np.median(temperature_c)
```

returns the middle value after considering the ordered data.

### Standard Deviation

```python
np.std(temperature_c)
```

provides a measure of how much the values vary around the mean.

These operations are useful for understanding the general behavior of sensor data.

---

# 11. Boolean Filtering

Boolean filtering allows numerical data to be selected according to a condition.

Example:

```python
high_temperature = temperature_c[temperature_c > 26]
```

This selects only temperature values greater than 26°C.

Another condition used was:

```python
normal_temperature = temperature_c[
    (temperature_c >= 25) & (temperature_c <= 27)
]
```

This selects readings between 25°C and 27°C.

Internally, NumPy creates Boolean values such as:

```text
True
False
True
True
False
```

Only the values corresponding to `True` are selected.

This technique is important for telemetry validation and identifying values that meet or violate predefined conditions.

---

# 12. Two-Dimensional NumPy Arrays

A two-dimensional NumPy array can represent data in rows and columns.

A sensor matrix was created containing example:

- Temperature
- Pressure
- Voltage

Example structure:

```text
Temperature   Pressure   Voltage
24.5          1012.3     11.8
25.1          1011.8     11.9
26.3          1011.2     12.0
27.0          1010.7     12.1
26.7          1010.9     12.0
```

The array shape was:

```text
(5, 3)
```

This means:

- 5 rows
- 3 columns

A two-dimensional structure is useful for representing multiple sensor parameters across multiple readings.

---

# 13. Extracting Sensor Columns

Specific columns were extracted from the 2D array.

For example:

```python
sensor_data[:, 0]
```

selects the first column.

Similarly:

```python
sensor_data[:, 1]
```

selects the second column.

And:

```python
sensor_data[:, 2]
```

selects the third column.

The `:` means all rows.

Therefore:

```python
sensor_data[:, 0]
```

means:

> Select all rows from column 0.

This concept is useful when individual sensor parameters need to be processed separately.

---

# 14. Vectorized Numerical Processing

Vectorization is one of the most important concepts studied during Day 3.

Vectorization means applying a numerical operation to an entire array instead of explicitly writing a Python loop for every individual element.

For example:

```python
calibrated_temperature = temperature_c * 1.02 + 0.5
```

The complete temperature array is processed at once.

Without vectorization, the same operation would normally require a loop.

Vectorized processing makes numerical code:

- Shorter
- Easier to understand
- Suitable for large numerical arrays
- Generally more efficient for array-based operations

For a Data Engineer working with telemetry, vectorization is particularly useful because datasets can contain many thousands or millions of numerical readings.

---

# 15. Vectorized Calibration Example

A simple calibration transformation was applied:

```python
calibrated_temperature = temperature_c * 1.02 + 0.5
```

The operation applies the same mathematical transformation to every reading.

The calculation can be understood as:

```text
Calibrated value = Original value × 1.02 + 0.5
```

Instead of processing each sensor reading manually, NumPy performs the calculation across the complete array.

This demonstrates how numerical transformations can be implemented as reusable processing routines.

---

# 16. Loop vs Vectorized Processing

A performance comparison was performed between:

1. A normal Python loop
2. A NumPy vectorized operation

One million numerical values were generated.

The loop approach processed each value individually:

```python
for value in data:
    loop_result.append(value * 2)
```

The vectorized approach used:

```python
vectorized_result = data * 2
```

Execution time was measured using:

```python
time.perf_counter()
```

The practical demonstrated that NumPy vectorized processing can perform large numerical operations efficiently compared with explicitly iterating through each value in Python.

The exact execution time depends on the computer, Python version, operating system and current system load. Therefore, the actual benchmark result generated on the local machine was retained in the notebook.

---

# 17. Synthetic Telemetry Generation

Synthetic telemetry data was generated because real operational data was not required for this training task.

The following parameters were generated:

- Temperature
- Pressure
- Voltage
- Altitude
- Speed

Example:

```python
temperature = np.random.uniform(20, 35, samples)
pressure = np.random.uniform(990, 1030, samples)
voltage = np.random.uniform(11, 13, samples)
altitude = np.random.uniform(100, 500, samples)
speed = np.random.uniform(20, 80, samples)
```

A total of 1000 synthetic samples were generated.

The data is intended only for numerical-processing demonstration and testing.

---

# 18. Reproducibility Using Random Seed

The following statement was used:

```python
np.random.seed(42)
```

A random seed makes the generated pseudo-random sequence reproducible.

This means that when the notebook is executed again using the same setup and code, the same synthetic sequence can be generated.

Reproducibility is important in engineering and data processing because testing should ideally be repeatable.

---

# 19. Synthetic Telemetry Statistical Analysis

After generating the synthetic telemetry, basic statistics were calculated.

For example:

```python
np.mean(temperature)
np.min(temperature)
np.max(temperature)
```

Similar calculations were performed for:

- Pressure
- Voltage
- Altitude
- Speed

This provides a basic numerical summary of the generated telemetry.

The analysis helps verify that the generated values remain within their intended ranges.

---

# 20. Telemetry Validation Using NumPy

Telemetry validation was implemented using Boolean conditions.

For example:

```python
temperature_valid = (
    (temperature >= 20) &
    (temperature <= 35)
)
```

Similar checks were applied to:

```text
Pressure: 990 to 1030
Voltage: 11 to 13
Altitude: 100 to 500
Speed: 20 to 80
```

The result of each condition is a Boolean array.

For example:

```text
True
True
False
True
...
```

The number of valid readings was counted using:

```python
np.sum(temperature_valid)
```

Boolean `True` values can be counted by NumPy as numerical ones, allowing the number of valid readings to be calculated.

This demonstrates a basic automated validation mechanism.

---

# 21. Broadcasting

Broadcasting is another important NumPy feature.

Broadcasting allows NumPy to perform operations between arrays with compatible shapes without manually repeating the smaller array.

Example:

```python
calibration_offset = np.array([
    0.5, 2.0, 0.1
])

calibrated_data = sensor_readings + calibration_offset
```

Here the three calibration values correspond to:

```text
Temperature → +0.5
Pressure    → +2.0
Voltage     → +0.1
```

NumPy automatically applies the offset to every corresponding row.

Broadcasting reduces the need for repetitive code and is useful for applying common transformations to sensor columns.

---

# 22. Numerical Processing Routine

A separate numerical processing routine was implemented to demonstrate common NumPy mathematical operations.

The routine used:

```python
data + 5
data * 2
data ** 2
np.sqrt(data)
```

These represent:

- Addition
- Multiplication
- Squaring
- Square root

The purpose was to understand how NumPy can perform different mathematical operations on an entire numerical array.

This provides a basic foundation for more complex numerical transformations used in data processing.

---

# 23. Complete Telemetry Matrix

The separate telemetry arrays were combined into a single matrix using:

```python
np.column_stack([
    temperature,
    pressure,
    voltage,
    altitude,
    speed
])
```

The resulting matrix represents multiple telemetry parameters together.

Conceptually:

```text
Temperature | Pressure | Voltage | Altitude | Speed
-----------------------------------------------------
    ...     |   ...    |   ...   |   ...    |  ...
    ...     |   ...    |   ...   |   ...    |  ...
    ...     |   ...    |   ...   |   ...    |  ...
```

This structure provides a convenient representation for numerical processing of multiple telemetry parameters.

---

# 24. Mean and Standard Deviation by Column

For the complete telemetry matrix, the mean was calculated using:

```python
np.mean(telemetry, axis=0)
```

The standard deviation was calculated using:

```python
np.std(telemetry, axis=0)
```

The `axis=0` argument means that the calculation is performed independently for each column.

Therefore, each telemetry parameter receives its own mean and standard deviation.

---

# 25. Numerical Normalization

The telemetry matrix was normalized using:

```python
normalized_telemetry = (
    telemetry - telemetry_mean
) / telemetry_std
```

Normalization transforms numerical values based on their mean and standard deviation.

The general formula is:

```text
Normalized Value =
(Value - Mean) / Standard Deviation
```

This is useful because different telemetry parameters can have very different numerical scales.

For example:

- Voltage may be around 12
- Pressure may be around 1000
- Altitude may be hundreds of units

Normalization can make numerical datasets easier to compare and can also be useful as preprocessing for later analytical or machine-learning tasks.

---

# 26. What Was Learned

During Day 3, the following concepts were studied and implemented:

1. NumPy library and its purpose
2. NumPy array creation
3. One-dimensional arrays
4. Two-dimensional arrays
5. Array shape, size and data type
6. Indexing
7. Slicing
8. Arithmetic operations
9. Statistical functions
10. Boolean filtering
11. Vectorization
12. Performance comparison
13. Broadcasting
14. Synthetic data generation
15. Random seed and reproducibility
16. Telemetry validation
17. Matrix creation
18. Column-wise processing
19. Numerical normalization

The practical demonstrated how NumPy can form the numerical-processing layer of an offline telemetry data pipeline.

---

# 27. Tools and Technologies Used

### Software

- Python 3.14.6
- Visual Studio Code
- PowerShell

### Python Library

- NumPy

### Python Concepts

- Arrays
- Indexing
- Slicing
- Mathematical operations
- Boolean conditions
- Random number generation
- Performance timing

### Engineering Concepts

- Numerical processing
- Vectorization
- Broadcasting
- Synthetic telemetry
- Data validation
- Reproducibility
- Normalization

---

# 28. Data Handling Approach

The practical followed an offline and synthetic-data approach.

No real operational telemetry was required.

The data was:

1. Generated locally
2. Stored in NumPy arrays
3. Numerically processed
4. Statistically analyzed
5. Validated using predefined ranges
6. Transformed using vectorized operations
7. Normalized for numerical analysis

This approach allows the processing logic to be tested safely before applying similar techniques to approved datasets.

---

# 29. Problems and Observations

No major blocking issue was encountered during the main NumPy practical after the Day 3 environment was successfully configured.

The main observations were:

- NumPy operations require compatible array shapes.
- Boolean conditions need proper use of operators such as `&`.
- Vectorized operations provide a simpler way to process complete arrays.
- Broadcasting works only when array shapes are compatible.
- Benchmark timings can vary between different systems and executions.
- Synthetic data is useful for testing processing logic without requiring real operational data.

---

# 30. Engineering Significance

The Day 3 task established the numerical-processing foundation for the Software & Data Engineer role.

Telemetry processing commonly involves large collections of numerical readings. Processing these readings efficiently is important for later stages such as:

```text
Data Generation
      ↓
Numerical Processing
      ↓
Validation
      ↓
Telemetry Processing
      ↓
ETL
      ↓
Auditing
      ↓
Analysis
```

NumPy provides the basic numerical-processing capabilities required before moving to higher-level data-processing tools such as Pandas.

The vectorization concepts learned today are especially important because they reduce the need for repeated Python-level loops when processing numerical arrays.

---

# 31. Output Files

The primary Day 3 output is:

```text
Day3/
└── NumPy_Numerical_Processing.ipynb
```

The documentation file is:

```text
Day3/
└── 03_numpy_numerical_processing_notes.md
```

The Day 3 virtual environment is:

```text
Day3/
└── .venv/
```

The `.venv` directory should not be committed to GitHub because it contains the local Python environment.

---

# 32. Conclusion

Day 3 successfully covered NumPy numerical processing and vectorized numerical processing.

The practical started with basic NumPy arrays and gradually progressed to:

- Array manipulation
- Numerical calculations
- Statistical analysis
- Filtering
- Vectorization
- Broadcasting
- Performance comparison
- Synthetic telemetry generation
- Telemetry validation
- Normalization

The final notebook demonstrates how NumPy can be used to build a basic offline numerical-processing routine for synthetic telemetry data.

The knowledge gained during this task provides the foundation for the next stage of the data-processing workflow.

---

# 33. Next Task

**Date:** 08 October 2026

**Task:** Pandas Telemetry Processing

The next task will build on the NumPy foundation and focus on using Pandas for structured telemetry-data processing, tabular data handling, cleaning, filtering and analysis.

The expected output will be a **Pandas data-processing notebook**.