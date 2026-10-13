# Day 10 — Performance Benchmarking: Loop vs Vectorized Processing

## 1. Introduction

Performance benchmarking is the process of measuring and comparing the execution performance of different implementations of the same computational task. It helps determine which approach processes data faster, how much data it can handle per second, and whether both implementations produce equivalent results.

In the RUDRAEDGE RE-T1 project context, software may need to process numerical information received from multiple sensors. Such information can include temperature, pressure, voltage, altitude, and speed. Efficient processing is important when telemetry records arrive continuously or when large datasets must be analyzed.

This task focuses on comparing traditional Python loop-based processing with NumPy vectorized processing. Both approaches perform the same numerical operation on the same dataset, allowing their performance to be compared fairly.

## 2. Objective

The primary objective is to analyze the performance difference between Python loops and NumPy vectorization.

The specific objectives are:

- Understand the difference between sequential and vectorized numerical processing.
- Create a numerical dataset for repeatable testing.
- Execute the same calculation using two different approaches.
- Measure execution time using a high-resolution timer.
- Calculate processing throughput in elements per second.
- Compare the correctness of the outputs.
- Generate a structured JSON report containing benchmark results.
- Understand how efficient numerical processing can support telemetry data analysis.

## 3. Tools and Technologies

### Python

Python is the programming language used to implement the benchmark. It provides functions, loops, timing utilities, file operations, and support for numerical libraries.

### NumPy

NumPy is a numerical computing library used to create arrays and perform mathematical operations efficiently. Its vectorized operations allow calculations to be applied to entire arrays without writing an explicit Python loop for each element.

### time.perf_counter()

The `time.perf_counter()` function measures elapsed time with a high-resolution performance counter. It is suitable for measuring short code execution intervals.

The elapsed time is calculated as:

`Elapsed Time = End Time - Start Time`

### JSON

JSON stands for JavaScript Object Notation. It is a structured text format used to store information in key-value pairs.

The benchmark results are saved in JSON format so that execution times, throughput, speedup, dataset size, and correctness can be inspected later.

### pathlib

The `Path` class from Python's `pathlib` module helps create and manage file paths. It is used to save the generated benchmark report to the correct directory.

### datetime

The `datetime` module records the date and time associated with the benchmark report.

## 4. Understanding the Dataset

The benchmark uses a NumPy array containing 200,000 numerical elements.

A deterministic dataset is created using NumPy's random number generator with a fixed seed. This makes the input reproducible: running the program again creates the same sequence of input values when the generation method and parameters remain unchanged.

The array contains numerical values that represent a computational workload. It is not actual flight telemetry captured from a physical UAV.

For each element, the program performs the following calculation:

`result = value * 2 + 5`

For example, if the input value is 10, the result is 25. If the input value is 3, the result is 11.

Both implementations perform this same operation, making it possible to compare their execution performance.

## 5. Loop-Based Processing

The first implementation uses a conventional Python loop.

In this approach, the program accesses one element at a time, performs the mathematical calculation, and stores the result in the corresponding output position.

The general procedure is:

1. Create an output array.
2. Iterate through the input array using an index.
3. Read the current element.
4. Multiply the element by 2 and add 5.
5. Store the calculated value.
6. Repeat until all elements have been processed.

This approach is easy to understand and useful when each record requires complicated conditional logic or when processing must follow a sequential procedure.

However, a Python loop performs repeated interpreter-level operations for individual elements. When the dataset becomes large, this overhead can increase the total execution time.

## 6. NumPy Vectorized Processing

The second implementation uses NumPy vectorization.

Instead of explicitly iterating through every element in Python, the calculation is applied directly to the entire NumPy array.

The operation is expressed as:

`result = data * 2.0 + 5.0`

NumPy applies the arithmetic operations to the array elements and returns a resulting array.

Vectorization reduces the need for repeated Python-level loop operations. Numerical libraries such as NumPy can perform array calculations through optimized underlying implementations.

This often makes vectorized processing faster for large numerical datasets.

However, vectorization is not guaranteed to be faster for every possible workload. Performance depends on the operation, array size, data types, memory requirements, and computing environment.

## 7. Benchmarking Methodology

The benchmark follows a controlled process.

### Step 1: Prepare the input

A numerical array containing 200,000 elements is generated.

### Step 2: Execute loop-based processing

The loop-based function processes the array and returns the computed results.

### Step 3: Execute vectorized processing

The vectorized function processes the same input array using NumPy operations.

### Step 4: Repeat the measurements

Each implementation is executed three times. The average execution time is calculated to reduce the influence of a single unusually fast or slow run.

The average is calculated as:

`Average Time = Sum of Measured Times / Number of Runs`

### Step 5: Calculate throughput

Throughput represents the number of elements processed per second.

`Throughput = Number of Elements / Average Execution Time`

Higher throughput indicates that more elements were processed per second during the measured interval.

### Step 6: Calculate speedup

The speedup factor compares the average execution time of the loop-based implementation with the vectorized implementation.

`Speedup = Loop Average Time / Vectorized Average Time`

A speedup greater than 1 means the vectorized implementation was faster in the measured test.

### Step 7: Verify correctness

The program uses NumPy's `allclose()` function to check whether the two result arrays contain numerically matching values within an accepted tolerance.

The report stores the outcome as a Boolean value: `True` or `False`.

### Step 8: Save the report

The measurements are organized into a Python dictionary and written to `benchmark_report.json` using JSON serialization.

## 8. Experimental Results

The completed benchmark produced the following output:

| Metric | Python loop | NumPy vectorization |
|---|---:|---:|
| Dataset size | 200,000 elements | 200,000 elements |
| Average execution time | 0.097183 seconds | 0.004300 seconds |
| Throughput | 2,057,982.28 elements/sec | 46,509,464.68 elements/sec |

The measured speedup factor was **22.6×**, and the result comparison returned `True`.

### Interpretation

The Python loop required approximately 0.097183 seconds to process the dataset. The vectorized implementation required approximately 0.004300 seconds.

For this specific test, vectorized processing completed the calculation in less time and achieved a higher throughput.

The speedup factor indicates that the loop-based execution time was approximately 22.6 times the vectorized execution time.

The `Results match: True` output indicates that the two implementations produced numerically matching results under the comparison performed by the program.

These measurements describe the particular dataset, calculation, Python and NumPy versions, and computer used for the test. They should not be treated as universal performance figures.

## 9. Understanding the JSON Report

The generated file is:

`Day10/codes/benchmark_report.json`

The report stores the following information:

- **Task:** The name of the performance benchmarking task.
- **Created timestamp:** The time at which the report was generated, including its timezone offset.
- **Dataset elements:** The number of numerical elements processed.
- **Operation:** The mathematical calculation applied to the input.
- **Loop metrics:** Average execution time and processing throughput for the loop-based method.
- **Vectorized metrics:** Average execution time and processing throughput for NumPy vectorization.
- **Speedup factor:** The ratio between the two average execution times.
- **Results match:** Whether the two implementations produced matching numerical results.

Saving the measurements in a structured report makes the experiment easier to inspect, share, and reproduce.

## 10. Relevance to UAV Telemetry Processing

A UAV software system may receive numerical information from several sensors. Processing this information efficiently can help downstream components analyze telemetry without unnecessary computational overhead.

For example, array-based processing may be useful for:

- Applying mathematical transformations to sensor readings.
- Processing large historical telemetry datasets.
- Calculating statistics across multiple records.
- Preparing numerical arrays for further analysis.
- Supporting data validation and preprocessing stages.

The current benchmark demonstrates the performance difference between two approaches to numerical computation. It provides a foundation for more advanced experiments involving multiple sensor columns, invalid readings, missing values, calibration, and data validation.

The benchmark itself does not establish that the same speedup will occur on a live UAV or that a particular processing rate satisfies real-time flight requirements. Those conclusions require measurements using representative workloads and the intended hardware.

## 11. Limitations

The experiment has several limitations.

First, the dataset is a generated numerical array rather than a recorded UAV telemetry dataset.

Second, the calculation is relatively simple. More complex algorithms may produce different performance results.

Third, the test uses three repetitions. More repetitions and additional statistical measurements could provide a more comprehensive understanding of performance variability.

Fourth, the reported throughput describes the measured processing function, not the complete telemetry pipeline. It does not include sensor communication, network transfer, file ingestion, or storage time.

Finally, the benchmark compares execution time and numerical correctness, but the original implementation does not measure peak memory usage or evaluate different dataset sizes.

These limitations should be considered before using the findings to make engineering decisions.

## 12. Possible Future Improvements

The benchmark can be extended in several ways:

1. Test multiple dataset sizes, such as 10,000, 100,000, and 1,000,000 elements.
2. Increase the number of repetitions and report the median as well as the average.
3. Compare processing time for multiple sensor columns.
4. Introduce missing readings and out-of-range values.
5. Measure memory consumption using a clearly defined measurement method.
6. Compare processing performance for different numerical data types.
7. Benchmark data validation and calibration operations.
8. Test on the intended hardware before making real-time performance claims.
9. Store results from repeated experiments to compare performance across software versions.

## 13. Conclusion

The performance benchmarking task compared Python loop-based processing with NumPy vectorized processing using the same numerical operation and input dataset.

The measured vectorized implementation achieved a speedup factor of approximately 22.6× in this experiment. Both implementations produced matching numerical results, confirming that the observed performance difference did not arise from an obvious difference in the calculation.

The benchmark demonstrates why vectorization is a useful technique for numerical data processing and provides a reproducible starting point for more comprehensive telemetry-processing performance tests.

The execution measurements were saved in a structured JSON report for inspection and further analysis.
