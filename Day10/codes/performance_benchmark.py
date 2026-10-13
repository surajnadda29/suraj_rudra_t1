
import time
import numpy as np
import json
from pathlib import Path
from datetime import datetime

# Output files will be saved in the Day10/codes folder
OUTPUT_DIR = Path(__file__).resolve().parent
REPORT_FILE = OUTPUT_DIR / "benchmark_report.json"


def loop_processing(data):
    """Process each element one by one using a Python loop."""
    result = np.empty(len(data), dtype=np.float64)

    for i in range(len(data)):
        result[i] = data[i] * 2.0 + 5.0

    return result


def vectorized_processing(data):
    """Process all elements using NumPy vectorized operations."""
    return data * 2.0 + 5.0


def benchmark(function, data, repeats=3):
    """Measure execution time and calculate throughput."""
    times = []

    for _ in range(repeats):
        start = time.perf_counter()
        result = function(data)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    average_time = sum(times) / len(times)
    throughput = len(data) / average_time if average_time > 0 else 0

    return {
        "average_time_seconds": round(average_time, 6),
        "throughput_elements_per_second": round(throughput, 2),
        "result": result
    }


def main():
    # Generate reproducible synthetic numerical data
    rng = np.random.default_rng(42)
    data = rng.random(200_000, dtype=np.float64)

    print("PERFORMANCE BENCHMARKING")
    print("-" * 40)
    print(f"Number of elements: {len(data):,}")

    loop_result = benchmark(loop_processing, data)
    vector_result = benchmark(vectorized_processing, data)

    # Check that both methods produce the same values
    results_match = np.allclose(
        loop_result["result"],
        vector_result["result"]
    )

    loop_time = loop_result["average_time_seconds"]
    vector_time = vector_result["average_time_seconds"]

    speedup = (
        loop_time / vector_time
        if vector_time > 0 else None
    )

    report = {
        "task": "Performance Benchmarking",
        "created_at_utc": datetime.now().astimezone().isoformat(),
        "dataset_elements": len(data),
        "operation": "result = value * 2 + 5",
        "loop": {
            "average_time_seconds": loop_time,
            "throughput_elements_per_second":
                loop_result["throughput_elements_per_second"]
        },
        "vectorized": {
            "average_time_seconds": vector_time,
            "throughput_elements_per_second":
                vector_result["throughput_elements_per_second"]
        },
        "speedup_factor": round(speedup, 2) if speedup else None,
        "results_match": bool(results_match)
    }

    REPORT_FILE.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8"
    )

    print(f"Loop average time      : {loop_time:.6f} seconds")
    print(f"Vectorized average time: {vector_time:.6f} seconds")
    print(f"Loop throughput        : "
          f"{loop_result['throughput_elements_per_second']:,.2f} elements/sec")
    print(f"Vector throughput      : "
          f"{vector_result['throughput_elements_per_second']:,.2f} elements/sec")
    print(f"Speedup factor         : {report['speedup_factor']}x")
    print(f"Results match          : {results_match}")
    print(f"Report saved           : {REPORT_FILE}")


if __name__ == "__main__":
    main()
