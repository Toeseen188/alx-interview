#!/usr/bin/python3
""" A script to search a log entry and print selected line """
import sys
import re
from collections import defaultdict

# Regular expression to match the input format
log_pattern = re.compile(
        r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

# Variables to store statistics
total_size = 0
status_counts = defaultdict(int)

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            ip, status_code, file_size = match.groups()
            status_counts[status_code] += 1
            total_size += int(file_size)
            line_count += 1
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_counts):
                print(f"{status_code}: {status_counts[status_code]}")
        if line_count % 10 == 0:
            line_count = 0
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass

# Print the final statistics
print("Total file size:", total_size)
for status_code in sorted(status_counts):
    print(f"{status_code}: {status_counts[status_code]}")
