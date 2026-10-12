# Day 9 — Auditing and Logging Framework

**Project:** RUDRAEDGE RE-T1 (Spectra)  
**Engineer:** Suraj Nadda  
**Role:** Software & Data Engineer  
**Task Date:** 13 October 2026  
**Task Name:** Auditing and Logging Framework

---

## 1. Introduction

In software development, a program should not only perform its assigned operations but should also maintain a record of what it does. If an operation fails, developers need enough information to understand what happened and identify the cause.

Auditing and logging help maintain this information. They make a program easier to monitor, troubleshoot, test, and maintain.

For this task, a Python-based Auditing and Logging Framework was developed. It records application activities, converts log events into structured JSON, captures a controlled test error with its traceback, and creates a summary of the execution.

The program generates its output locally inside the `Day9/codes/` directory.

The practical focuses on three main areas:

1. System auditing
2. Structured JSON logging
3. Error trace capturing

The expected outcome is a working audit-log system that records events in a consistent format and helps verify the execution of the application.

## 2. Objective of the Task

The main objective is to develop and test a basic audit-log system using Python.

The specific objectives are:

- Record important application activities.
- Maintain a timestamp for each recorded event.
- Identify the event type, actor, action, and status.
- Store events in structured JSON format.
- Capture exception details and traceback information.
- Verify that the generated log entries contain valid JSON.
- Generate a JSON summary of the execution.
- Keep all generated files within the task's own folder.
- Demonstrate how logs can help identify and investigate errors.

This practical demonstrates the basic principles of application auditing and logging. It does not implement a complete operating-system auditing service.

## 3. Practical Scope

### 3.1 System Auditing

System auditing means maintaining records of important activities performed by a system or application. These records help determine what happened, when it happened, which component performed the action, and whether the operation succeeded.

In this practical, auditing is performed at the application level.

The program records events such as:

- Starting the audit system.
- Starting a sample telemetry-validation operation.
- Completing sample data validation.
- Capturing a controlled test error.
- Preparing the audit-log output.
- Completing the audit system.

For example, if a program starts a validation operation, an audit event can record the action and its status. If an error occurs, a separate event records that the error was captured.

**Why is auditing important?**

Auditing helps developers understand the sequence of operations performed by an application. It is useful for troubleshooting, reviewing application behavior, identifying repeated failures, and maintaining an execution history.

In a real production system, audit records may also be used to investigate unauthorized changes or suspicious activities. Such use requires additional security controls, access restrictions, and protection against log tampering.

### 3.2 Structured JSON Logging

Logging is the process of recording messages and events generated during program execution.

Structured logging stores information in a consistent, machine-readable format rather than saving only unstructured text messages.

JSON stands for JavaScript Object Notation. It represents information using objects, key-value pairs, arrays, strings, numbers, Boolean values, and other supported data types.

A structured log event in this project contains fields such as:

- `timestamp`
- `level`
- `event_type`
- `actor`
- `action`
- `status`
- `details`

A simplified example is:

```json
{
    "timestamp": "2026-10-12T15:22:34+00:00",
    "level": "INFO",
    "event_type": "user_action",
    "actor": "suraj_rudra_task",
    "action": "Started sample telemetry validation",
    "status": "SUCCESS",
    "details": {
        "source": "synthetic demonstration data"
    }
}
```

This example illustrates the format; the timestamp and values in an actual log depend on the recorded event.

**Why use structured JSON logs?**

1. They are easier for programs to read than free-form text.
2. They can be searched and filtered by fields.
3. They allow different event types to use a consistent structure.
4. They can be processed later by Python scripts or log-analysis tools.
5. They make it easier to summarize events by status or type.

The program saves these records in a JSON Lines file. Each line contains one complete JSON object.

### 3.3 Error Trace Capturing

Errors can occur because of invalid input, incorrect calculations, missing files, unavailable resources, or programming mistakes.

When an exception occurs, the exception message alone may not explain where the problem originated. A traceback provides information about the sequence of function calls leading to the error.

This practical demonstrates error trace capturing by deliberately triggering a controlled division-by-zero exception.

The program catches the exception and records:

- The exception type.
- The exception message.
- The traceback.
- The event type.
- The action associated with the error.
- A status indicating that the error was captured.

The error is intentionally generated for testing. It is caught by the program, so the entire program can continue and complete its logging workflow.

**Why is traceback information useful?**

It helps developers identify the location and execution path associated with a failure. This makes debugging easier than relying only on a short error message.

A traceback may contain file paths, function names, and other implementation details. In production applications, such information should be protected from unauthorized users.

## 4. Understanding the ETL and Auditing Relationship

The previous Day 8 task focused on ETL Pipeline Assembly. ETL stands for Extract, Transform, and Load.

Day 9 has a different primary objective: recording and examining application events.

The two tasks are related because a data-processing pipeline can produce audit events during its execution.

For example:

- When data extraction begins, a start event can be recorded.
- When validation finishes, a validation event can be recorded.
- When a file is saved, a file-operation event can be recorded.
- When an exception occurs, an error event can be recorded.

In this Day 9 demonstration, the program records sample telemetry-related activities. It does not automatically connect to or execute the Day 8 ETL pipeline. The two tasks remain separate.

## 5. System Architecture

The program follows a simple sequence:

```text
Start Program
     |
     v
Configure Python Logger
     |
     v
Record Application Events
     |
     v
Capture Controlled Test Error
     |
     v
Write Structured JSON Log
     |
     v
Read and Validate Log Entries
     |
     v
Generate Audit Summary
     |
     v
Display Execution Results
```

### Explanation of the architecture

**Step 1 — Start program:** Python begins executing the main script.

**Step 2 — Configure logger:** The program prepares a logger and a file handler to write events to the audit-log file.

**Step 3 — Record events:** The program records activities with timestamps, event types, actors, actions, statuses, and details.

**Step 4 — Capture an error:** A controlled exception is triggered and caught. The logger records the exception and traceback.

**Step 5 — Write structured logs:** Each event is serialized into JSON and written as a separate line in the log file.

**Step 6 — Validate log entries:** The program reads the log file and parses each line using Python's JSON parser.

**Step 7 — Generate summary:** The program calculates summary information, including the number of events and captured errors.

**Step 8 — Display results:** The program prints the result and the paths of the generated files.

## 6. Tools and Libraries Used

The task uses Python's built-in libraries, so additional packages are not required for the logging framework.

### 6.1 Python

Python is the programming language used to implement the audit system.

It provides functions, classes, exception handling, file operations, and libraries that support structured logging.

### 6.2 `logging`

The `logging` module records events generated by the program.

It supports different severity levels:

- `DEBUG` — detailed information used during debugging.
- `INFO` — normal application activity.
- `WARNING` — an unexpected condition that may require attention.
- `ERROR` — an operation has failed.
- `CRITICAL` — a severe failure that may prevent the application from continuing.

The project configures its logger at the `INFO` level. The controlled exception is recorded using `logger.exception()`, which records the error event and exception information.

### 6.3 `json`

The `json` module converts Python objects into JSON strings and reads JSON data back into Python objects.

The program uses:

- `json.dumps()` to serialize an event into a JSON string.
- `json.loads()` to parse each recorded JSON line.
- `json.dumps(..., indent=4)` to write a formatted JSON summary.

Parsing the log entries successfully demonstrates that the entries are valid JSON. It does not, by itself, prove that every event contains all the correct business information.

### 6.4 `traceback`

The `traceback` module provides utilities for formatting exception tracebacks.

The program uses `traceback.format_exception()` to obtain a readable representation of the exception and its traceback. This text is then included in the error event.

### 6.5 `datetime` and `timezone`

The `datetime` module provides date and time functionality.

The program uses `datetime.now(timezone.utc)` to create a timezone-aware UTC timestamp.

UTC means Coordinated Universal Time. Recording timestamps in UTC provides a consistent reference when systems operate in different time zones.

For example, the summary contains:

```text
2026-10-12T15:22:34.794525+00:00
```

This represents a UTC timestamp. It is equivalent to 8:52:34.794525 PM on 12 October 2026 in India Standard Time.

### 6.6 `pathlib`

The `pathlib` module provides an object-oriented way to work with file paths.

The program uses `Path(__file__).resolve().parent` to identify the directory containing the Python script. It then creates paths for the audit log and summary files.

This approach avoids depending on whichever directory happens to be open in the terminal.

### 6.7 Visual Studio Code

Visual Studio Code is used to create and edit the Python script, run it in the integrated terminal, and inspect the generated files.

### 6.8 Python built-ins

The program also uses built-in features such as:

- Classes and methods.
- Dictionaries.
- Functions.
- File reading and writing.
- `try` and `except`.
- Exception objects.
- List comprehensions.
- Conditional expressions.

These features help implement the logging workflow without additional dependencies.

## 7. Project Folder Structure

The Day 9 task is maintained separately from the earlier tasks.

```text
suraj_rudra_task/
└── Day9/
    ├── codes/
    │   ├── audit_system.py
    │   ├── audit_log.jsonl
    │   └── audit_summary.json
    ├── notes/
    │   └── 09_auditing_logging_notes.md
    └── logs/
        └── daily_diary.md
```

### Folder responsibilities

**`codes/`**

Contains the Python source code and the generated output files. The audit log and summary are saved here so that the task is self-contained.

**`notes/`**

Contains technical documentation explaining the purpose, design, implementation, and results of the practical.

**`logs/`**

Contains the daily engineering diary. The diary records the assigned task, work completed, tools used, output paths, problems, resolutions, and next task.

This structure keeps the code, explanatory notes, and daily record organized.

## 8. Explanation of the Python Program

### 8.1 Importing the required modules

```python
import json
import logging
import traceback
from datetime import datetime, timezone
from pathlib import Path
```

Each import provides a specific capability.

- `json` handles JSON conversion and parsing.
- `logging` records events.
- `traceback` formats error trace information.
- `datetime` and `timezone` provide timestamps.
- `Path` handles file paths.

Importing a module makes its available functions and classes accessible to the program.

### 8.2 Defining the output directory

```python
BASE_DIR = Path(__file__).resolve().parent
AUDIT_FILE = BASE_DIR / "audit_log.jsonl"
SUMMARY_FILE = BASE_DIR / "audit_summary.json"
```

`__file__` refers to the current Python script.

`resolve()` produces a resolved path, and `parent` identifies the directory containing that script.

The `/` operator on a `Path` object joins a directory with a filename.

As a result, the program stores its outputs in the same directory as `audit_system.py`.

### 8.3 Creating the JSON formatter

A class groups related behavior. Here, `JSONFormatter` extends Python's `logging.Formatter` class and changes how each logging record is formatted.

The `format()` method receives a logging record and builds a dictionary containing the required event fields.

**`record.levelname`**

Provides the logging severity level, such as `INFO`.

**`getattr()`**

Retrieves an attribute from an object. If the attribute is missing, it returns the supplied default value.

For example:

```python
getattr(record, "actor", "system")
```

returns the record's `actor` attribute if it exists. Otherwise, it returns `"system"`.

**`record.getMessage()`**

Retrieves the message associated with the logging record.

**`record.exc_info`**

Contains exception information when the logging call includes an active exception.

When exception information exists, the formatter adds an `error` object containing the exception type, message, and formatted traceback.

Finally, `json.dumps()` converts the dictionary into a JSON string. The `ensure_ascii=False` option allows non-ASCII characters to be written directly instead of unnecessarily escaping them.

### 8.4 Configuring the logger

```python
logger = logging.getLogger("day9_audit")
logger.setLevel(logging.INFO)
logger.handlers.clear()
logger.propagate = False

file_handler = logging.FileHandler(
    AUDIT_FILE, mode="w", encoding="utf-8"
)
file_handler.setFormatter(JSONFormatter())
logger.addHandler(file_handler)
```

`logging.getLogger("day9_audit")` retrieves the named logger.

`setLevel(logging.INFO)` sets the minimum severity level handled by this logger to `INFO`. It will therefore also handle higher-severity levels such as `WARNING` and `ERROR`.

`handlers.clear()` removes existing handlers from this named logger. This helps prevent duplicate output when the configuration is run repeatedly in the same Python process.

`propagate = False` prevents the logger's records from being passed to its parent logger.

`FileHandler` writes logging records to a file. The `mode="w"` setting opens the file for writing and replaces its previous contents when the handler is initialized.

The `encoding="utf-8"` setting specifies the text encoding.

`setFormatter(JSONFormatter())` connects the custom formatter to the handler, and `addHandler()` attaches the handler to the logger.

**Important:** This configuration starts a fresh log for each run. It is suitable for a repeatable demonstration, but a production audit system would need an explicit retention policy, controlled access, and an appropriate append or rotation strategy.

### 8.5 Defining the audit-event function

```python
def audit_event(event_type, action, status="SUCCESS", details=None):
    logger.info(
        action,
        extra={
            "event_type": event_type,
            "actor": "suraj_rudra_task",
            "action": action,
            "status": status,
            "details": details or {},
        },
    )
```

This function provides a consistent way to record normal application events.

Its parameters are:

- `event_type`: identifies the category of event.
- `action`: describes what happened.
- `status`: identifies the outcome.
- `details`: provides additional information about the event.

The `extra` parameter adds custom attributes to the logging record. The custom formatter reads these attributes and includes them in the JSON object.

The expression `details or {}` uses an empty dictionary when no details are supplied.

This function reduces repeated code and helps keep event records consistent.

### 8.6 Capturing a controlled error

```python
def demonstrate_error_capture():
    try:
        value = 10 / 0
        return value
    except Exception:
        logger.exception(
            "Controlled test error captured",
            extra={
                "event_type": "error_trace",
                "actor": "suraj_rudra_task",
                "action": "demonstrate_error_capture",
                "status": "ERROR_CAPTURED",
                "details": {
                    "purpose": "Verify exception and traceback logging"
                },
            },
        )
        return None
```

The function deliberately attempts to divide 10 by zero. Python raises a `ZeroDivisionError`.

The `try` block contains the operation that may fail. The `except` block handles the resulting exception.

`logger.exception()` is designed for use inside an exception handler. It logs the supplied message and includes the active exception information.

The custom formatter uses that information to create the `error` object.

The status `ERROR_CAPTURED` means that the error was caught and recorded; it does not mean that the division operation succeeded.

The function returns `None` after capturing the error, allowing the main program to continue.

This is a controlled test, not a real system failure. In an actual application, exception handling should be designed around the operations that may fail and the appropriate recovery behavior.

### 8.7 The main function

```python
def main():
```

The `main()` function coordinates the execution sequence.

It records the start event, a sample validation event, the controlled error, and a file-operation event. It then reads the log entries, creates the summary, records the completion event, and prints the results.

Separating the workflow into a function makes the program easier to read, test, and maintain.

### 8.8 Recording events

For example:

```python
audit_event(
    "data_validation",
    "Sample validation completed",
    details={
        "records_checked": 10,
        "records_accepted": 9,
        "records_rejected": 1
    },
)
```

This event records a demonstration of data validation.

The values indicate that 10 sample records were checked, with 9 accepted and 1 rejected. These are illustrative values created by the program; they are not actual results from the Day 8 dataset.

### 8.9 Flushing the log handler

```python
for handler in logger.handlers:
    handler.flush()
```

A logging handler may buffer output before writing it completely.

`flush()` asks the handler to write buffered output to its destination. The program flushes the log before reading it so that the verification step can access the events already recorded.

Flushing is not the same as making a log tamper-proof or guaranteeing durability against every possible system failure.

### 8.10 Reading and validating the log

```python
entries = []
with AUDIT_FILE.open("r", encoding="utf-8") as file:
    for line in file:
        entries.append(json.loads(line))
```

The program opens the log file in read mode.

The `with` statement manages the file resource and closes it automatically when the block finishes.

Each line is parsed with `json.loads()`. If a line contains invalid JSON, parsing raises an exception.

The parsed objects are stored in the `entries` list.

This demonstrates basic JSON syntax validation. A more advanced validator could also check that each event has the required fields and that their values have the expected types.

### 8.11 Creating the audit summary

```python
summary = {
    "run_time_utc": datetime.now(timezone.utc).isoformat(),
    "total_events": len(entries),
    "successful_events": sum(
        1 for entry in entries
        if entry["status"] == "SUCCESS"
    ),
    "captured_errors": sum(
        1 for entry in entries
        if entry["event_type"] == "error_trace"
    ),
    "json_validation": "PASSED",
    "audit_log_file": AUDIT_FILE.name,
}
```

The summary is a compact report of the run.

`len(entries)` counts the log entries parsed at that stage.

The `sum()` expressions count entries that satisfy a condition:

- `successful_events` counts entries whose status is `SUCCESS`.
- `captured_errors` counts entries whose event type is `error_trace`.

The summary records the validation result and the log filename.

It is then saved using:

```python
SUMMARY_FILE.write_text(
    json.dumps(summary, indent=4),
    encoding="utf-8",
)
```

The `indent=4` setting formats the JSON with indentation, making it easier for a person to read.

### 8.12 Recording the final completion event

After writing the summary, the program records another event:

```python
audit_event(
    "system_event",
    "Audit system completed",
    details={"summary_file": SUMMARY_FILE.name},
)
```

This is a normal audit event that marks the completion of the logging workflow.

The program flushes the handler again so the final event is written to the log.

Because the summary is created **before** this final event, the summary does not include the completion event in its `total_events` count. This explains why the terminal reported 6 total events while the summary contained 5.

### 8.13 The entry-point condition

```python
if __name__ == "__main__":
    main()
```

When a Python file is run directly, Python sets its `__name__` value to `"__main__"`.

This condition calls `main()` when the script is executed directly. If the file is imported as a module by another Python program, the main workflow does not automatically run.

This is a common Python programming convention.

## 9. Understanding the Output Files

### 9.1 `audit_system.py`

This is the source-code file. It contains the logger configuration, JSON formatter, audit-event function, controlled error demonstration, summary generation, and execution workflow.

It can be edited and rerun to test changes to the framework.

### 9.2 `audit_log.jsonl`

This is the main audit-log output.

The `.jsonl` extension commonly refers to JSON Lines format, in which each line contains one independent JSON value, usually an object.

Unlike a single JSON array, a JSON Lines file can be processed one line at a time.

The log contains the recorded event fields and, for the controlled error, the exception type, message, and traceback.

It is the primary evidence that the program recorded the test events.

### 9.3 `audit_summary.json`

This file contains the summary generated during execution.

Your actual output was:

```json
{
    "run_time_utc": "2026-10-12T15:22:34.794525+00:00",
    "total_events": 5,
    "successful_events": 4,
    "captured_errors": 1,
    "json_validation": "PASSED",
    "audit_log_file": "audit_log.jsonl"
}
```

The fields mean:

- `run_time_utc`: the UTC time at which the summary was created.
- `total_events`: the number of log entries counted when the summary was generated.
- `successful_events`: the number of those entries marked `SUCCESS`.
- `captured_errors`: the number of entries identified as error-trace events.
- `json_validation`: confirms that the existing log entries parsed successfully.
- `audit_log_file`: identifies the log file associated with the summary.

The summary provides a quick view of the execution without requiring a person to read every log line.

## 10. Actual Execution Results

The terminal output received during testing was:

```text
AUDITING AND LOGGING FRAMEWORK
--------------------------------------
Total events      : 6
Captured errors   : 1
JSON validation   : PASSED
Audit log         : C:\Users\HP\OneDrive\Desktop\suraj_rudra_task\Day9\codes\audit_log.jsonl
Summary           : C:\Users\HP\OneDrive\Desktop\suraj_rudra_task\Day9\codes\audit_summary.json
```

The generated summary reported:

| Metric | Actual result |
|---|---:|
| Events counted in summary | 5 |
| Successful events | 4 |
| Captured errors | 1 |
| JSON validation | PASSED |
| Terminal event count | 6 |

### Interpretation of the results

**The program executed successfully.** The terminal output confirms that it reached the reporting stage and produced the output paths.

**The JSON validation passed.** The program was able to parse the log entries that existed at the validation stage.

**One error was captured.** The controlled division-by-zero exception was recorded as an error-trace event.

**The counts differ for an expected reason.** The summary is generated before the final completion event is recorded. The summary therefore counts five entries, whereas the terminal reports six after the final event has been written.

These results demonstrate the intended basic workflow. They do not prove that the system is secure against deliberate log modification or that it can monitor all operating-system activity.

## 11. Problems Encountered and Resolution

During the reported run, no execution failure was shown in the terminal output.

The controlled exception was intentional and served as a test of the error-capturing mechanism.

The event-count difference between the summary and the terminal is explained by the order of operations: the summary is written before the final completion event.

For future versions, the count could be made consistent by writing the final event before calculating the summary or by explicitly documenting that the summary excludes the completion event. If the summary is intended to represent the complete run, the program should be reorganized to count all events consistently.

## 12. Testing and Verification

The practical can be checked using the following tests.

### Test 1 — Normal event recording

Run the program and open `audit_log.jsonl`.

Expected result: the log contains events for the start of the system, the sample validation activity, the file operation, and completion.

### Test 2 — JSON parsing

The program reads each line using `json.loads()`.

Expected result: every existing line parses successfully. If a line is corrupted, parsing should fail rather than silently treating the invalid line as valid JSON.

### Test 3 — Error trace capture

Locate the event with:

```text
event_type = error_trace
```

Expected result: the event contains the controlled exception type, message, and traceback.

### Test 4 — Summary generation

Open `audit_summary.json`.

Expected result: the file contains a timestamp, event counts, the error count, a validation result, and the audit-log filename.

### Test 5 — Repeat execution

Run the script a second time and inspect the outputs.

Expected result: the script generates a fresh log because the file handler uses write mode. The previous run's log content is replaced.

This behavior is appropriate for a simple repeatable demonstration. A production audit system generally needs a deliberate strategy for retaining previous records.

## 13. Limitations of the Current Implementation

The current implementation is a basic demonstration rather than a production-grade auditing service.

Its limitations include:

1. **Application-level scope:** it records events explicitly generated by this program; it does not monitor all system activity.
2. **Controlled error:** the captured error is deliberately generated for testing.
3. **Log replacement:** the log file is overwritten at the start of each run.
4. **No tamper protection:** a person with write access to the file may modify or delete the log.
5. **No authentication:** the actor field is a fixed label, not a verified user identity.
6. **Basic validation:** the program verifies JSON parsing but does not enforce a complete schema for every field.
7. **Limited event coverage:** only the actions explicitly passed to the logger are recorded.
8. **No remote monitoring:** the program does not send events to a centralized monitoring service.
9. **No automatic alerting:** captured errors are logged, but they do not automatically generate notifications.
10. **Summary timing:** the summary excludes the final completion event because of the current execution order.

Recognizing these limitations is important because it distinguishes a working learning prototype from a hardened system used in production.

## 14. Future Improvements

The framework could be improved in several ways:

- Add a formal JSON schema or field-validation function.
- Record actual pipeline operations instead of demonstration events.
- Use log rotation or an append-only retention strategy.
- Add unique event IDs and correlation IDs.
- Use verified user or component identities for the actor field.
- Add automated tests for successful operations, invalid data, and exception handling.
- Ensure the summary accurately represents all recorded events.
- Restrict access to audit files.
- Store protected copies of logs or send them to a centralized logging service.
- Add filters and reports for errors, event types, and time ranges.
- Add monitoring and alerts for repeated failures.
- Avoid placing passwords, tokens, or other secrets in log entries.

For a production implementation, log integrity and access controls would be especially important because logs may be used during incident investigations.

## 15. Relevance to the RUDRAEDGE Project

Within the RUDRAEDGE RE-T1 (Spectra) project context, an audit-log system can help document the sequence of software and data-processing activities.

For example, an application that processes sensor telemetry could record when a processing stage starts, how many records it validates, when an output is saved, and whether an error occurs.

This information can help a developer understand the execution history and investigate failures.

The current Day 9 program demonstrates those concepts with sample application events. It is not connected to live sensors, actual flight telemetry, or an operating-system audit service.

A future integration could connect the same logging approach to the project's data-processing code, provided the event definitions, error-handling requirements, and data-protection controls are reviewed first.

## 16. Conclusion

The Day 9 Auditing and Logging Framework practical was implemented using Python's built-in logging, JSON, traceback, datetime, and pathlib modules.

The program records application events in structured JSON Lines format, captures a controlled exception with traceback information, reads and validates the generated log entries, and creates a JSON execution summary.

The reported test run produced the expected audit-log and summary files. JSON validation passed, and one controlled error was captured. The difference between the summary's five events and the terminal's six events is explained by the final completion event being recorded after the summary was generated.

The practical provides a foundation for understanding structured logging, application auditing, and error investigation. Further improvements would be needed before using the framework as a production-grade or security-critical audit service.

---

**Task Status:** Implemented and tested for the reported demonstration run.

**Expected Outcome:** Audit-log system — demonstrated through `audit_log.jsonl` and `audit_summary.json`.

**Output Directory:** `Day9/codes/`

**Engineer:** Suraj Nadda

**Role:** Software & Data Engineer