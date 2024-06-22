#!/usr/bin/python3
''' This defines a program to parse logs in real time '''

import sys
import re

fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_lines = 0
file_size = 0

try:
    while True:
        total_lines += 1

        match = re.fullmatch(fmt, input().strip())
        if match:
            try:
                file_size += int(match.group('file_size'))
                stat_code = int(match.group('status_code'))

                if stat_code and stat_code in status_codes:
                    status_codes[stat_code] += 1

                if total_lines % 10 == 0:
                    print(f"File size: {file_size}")
                    for key, val in sorted(status_codes.items()):
                        if val != 0:
                            print("{}: {}".format(key, val))

            except ValueError:
                continue

except (KeyboardInterrupt, EOFError):
    print(f"File size: {file_size}")
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))
