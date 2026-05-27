# Server Health Checker

A simple Python utility that inspects the local system health by checking CPU, memory, and disk usage, and records each run in a log file.

## Features

- Checks current CPU usage.
- Checks current memory usage.
- Checks current disk usage for the root (`/`) filesystem.
- Prints usage values and alerts when thresholds are exceeded.
- Appends a summary entry to `server_health_logs.txt` after every run.

## Requirements

- Python 3.7+
- `psutil`

## Installation

1. Clone the repository, or copy `server_health_checker.py` into your project folder.
2. Install the required Python package:

```bash
pip install psutil
```

## Usage

Run the script from the command line:

```bash
python server_health_checker.py
```

The script will display:

- CPU usage
- Memory usage
- Disk usage
- Any high-usage alerts when thresholds are exceeded

A log entry is also appended to `server_health_logs.txt` for each execution.

## Thresholds

The current alert thresholds are defined in `server_health_checker.py`:

- CPU: `80%`
- Memory: `80%`
- Disk: `90%`

## Notes

- The script checks the root filesystem (`/`) for disk usage.
- The log file is created or appended in the same directory where the script runs.
- This utility is best suited for basic local health checks or as a starting point for more advanced monitoring workflows.
