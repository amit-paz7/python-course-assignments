import sys
import re
from collections import defaultdict
from datetime import datetime

def create_activity_report(log_file, report_file):
   
    activity_totals = defaultdict(int)
    log_entry_pattern = re.compile(r"(\d{2}:\d{2})-(\d{2}:\d{2})\s+(.*)")

    print(f"Reading from '{log_file}'...")
    with open(log_file, 'r') as f_in:
        for line in f_in:
            match = log_entry_pattern.match(line.strip())
            if match:
                start_str, end_str, description = match.groups()
                
                time_format = "%H:%M"
                start_time = datetime.strptime(start_str, time_format)
                end_time = datetime.strptime(end_str, time_format)
                duration = (end_time - start_time).total_seconds() / 60
                activity_totals[description.strip()] += duration
                
    print(f"Writing report to '{report_file}'...")
    total_minutes = sum(activity_totals.values())
    
    max_len = 0
    if activity_totals:
        max_len = max(len(desc) for desc in activity_totals.keys())

    with open(report_file, 'w') as f_out:
        for activity, minutes in sorted(activity_totals.items()):
            if total_minutes > 0:
                percentage = (minutes / total_minutes) * 100
            else:
                percentage = 0

            line_to_write = (
                f"{activity:<{max_len}}  "
                f"{int(minutes):>4} minutes   "
                f"{int(round(percentage))}%"
            )
            f_out.write(line_to_write + "\n")

def main():
    if len(sys.argv) < 2:
        print("----------------------------------------------------")
        print("please provide the path to the log file.")
        print("Usage: python parse_timelog.py timelog.log")
        print("----------------------------------------------------")
        return

    log_filename = sys.argv[1]
    report_filename = "report.txt"

    try:
        create_activity_report(log_filename, report_filename)
        print("Report created successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{log_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
