import sys
import os


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3],
    }


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log["level"].upper() == level, logs))


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        lvl = log["level"].upper()
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print("Log Level | count")
    print("-----------------|----------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<16}| {counts.get(level, 0)}")


