
import json
import logging
import traceback
from datetime import datetime, timezone
from pathlib import Path


# All generated files stay in the same folder as this script.
BASE_DIR = Path(__file__).resolve().parent
AUDIT_FILE = BASE_DIR / "audit_log.jsonl"
SUMMARY_FILE = BASE_DIR / "audit_summary.json"


class JSONFormatter(logging.Formatter):
    """Convert each logging event into a structured JSON object."""

    def format(self, record):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "event_type": getattr(record, "event_type", "application_event"),
            "actor": getattr(record, "actor", "system"),
            "action": getattr(record, "action", record.getMessage()),
            "status": getattr(record, "status", "INFO"),
            "details": getattr(record, "details", {}),
        }

        if record.exc_info:
            event["error"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": "".join(
                    traceback.format_exception(*record.exc_info)
                ),
            }

        return json.dumps(event, ensure_ascii=False)


# Configure structured JSON logging.
logger = logging.getLogger("day9_audit")
logger.setLevel(logging.INFO)
logger.handlers.clear()
logger.propagate = False

file_handler = logging.FileHandler(
    AUDIT_FILE, mode="w", encoding="utf-8"
)
file_handler.setFormatter(JSONFormatter())
logger.addHandler(file_handler)


def audit_event(event_type, action, status="SUCCESS", details=None):
    """Record a normal audit event."""
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


def demonstrate_error_capture():
    """Trigger and capture a controlled example error."""
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


def main():
    # Start a fresh log for this demonstration run.
    audit_event(
        "system_event",
        "Audit system started",
        details={"task": "Day 9 Auditing and Logging Framework"},
    )

    audit_event(
        "user_action",
        "Started sample telemetry validation",
        details={"source": "synthetic demonstration data"},
    )

    audit_event(
        "data_validation",
        "Sample validation completed",
        details={"records_checked": 10, "records_accepted": 9,
                 "records_rejected": 1},
    )

    demonstrate_error_capture()

    audit_event(
        "file_operation",
        "Audit log output prepared",
        details={"file": AUDIT_FILE.name},
    )

    # Flush buffered entries before reading the file.
    for handler in logger.handlers:
        handler.flush()

    # Read the JSON Lines file and verify every entry.
    entries = []
    with AUDIT_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            entries.append(json.loads(line))

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

    SUMMARY_FILE.write_text(
        json.dumps(summary, indent=4),
        encoding="utf-8",
    )

    audit_event(
        "system_event",
        "Audit system completed",
        details={"summary_file": SUMMARY_FILE.name},
    )

    for handler in logger.handlers:
        handler.flush()

    print("AUDITING AND LOGGING FRAMEWORK")
    print("-" * 38)
    print(f"Total events      : {len(entries) + 1}")
    print(f"Captured errors   : {summary['captured_errors']}")
    print(f"JSON validation   : {summary['json_validation']}")
    print(f"Audit log         : {AUDIT_FILE}")
    print(f"Summary           : {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
