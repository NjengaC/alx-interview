#!/usr/bin/env python3

"""
Log parsing script that reads log entries from stdin, computes metrics,
and prints statistics on file size and status code occurrences.

Input format expected:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import re
from collections import defaultdict


# Regular expression to match the log format
LOG_PATTERN = re.compile(
r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')
# Status codes we are interested in
VALID_STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0


def main():
    """
    Main function to process log entries from stdin, calculate metrics,
    and print statistics on file size and status code occurrences.
    """
    try:
        for line in sys.stdin:
            line = line.strip()
            match = LOG_PATTERN.match(line)

            if match:
                ip_address, date, status_code, file_size = match.groups()

                # Calculate total file size
                file_size = int(file_size)
                total_file_size += file_size

                # Count status codes
                if status_code in VALID_STATUS_CODES:
                    status_code_count[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print(f"File size: {total_file_size}")
                    for code in sorted(status_code_count.keys()):
                        print(f"{code}: {status_code_count[code]}")
                    print()

    except KeyboardInterrupt:
        pass

    finally:
        print(f"File size: {total_file_size}")
        for code in sorted(status_code_count.keys()):
            print(f"{code}: {status_code_count[code]}")


if __name__ == "__main__":
    main()
