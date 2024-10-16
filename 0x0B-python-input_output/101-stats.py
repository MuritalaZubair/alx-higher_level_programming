#!/usr/bin/python3
"""Reads from standard input and computes log metrics."""

def display_metrics(total_size, status_count):
    """Display accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_count):
        print("{}: {}".format(code, status_count[code]))

if __name__ == "__main__":
    import sys

    total_size = 0
    status_count = {}
    valid_statuses = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_counter = 0

    try:
        for log_line in sys.stdin:
            line_counter += 1

            if line_counter % 10 == 0:
                display_metrics(total_size, status_count)

            parts = log_line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                continue

            try:
                status_code = parts[-2]
                if status_code in valid_statuses:
                    if status_code in status_count:
                        status_count[status_code] += 1
                    else:
                        status_count[status_code] = 1
            except IndexError:
                continue

        display_metrics(total_size, status_count)

    except KeyboardInterrupt:
        display_metrics(total_size, status_count)
        raise
