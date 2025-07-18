import csv
from datetime import datetime
import sys


def load_data(path):
    with open(path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def filter_by_date(rows, start_date=None, end_date=None):
    def parse_date(s):
        return datetime.strptime(s, '%Y-%m-%d').date()

    start = parse_date(start_date) if start_date else None
    end = parse_date(end_date) if end_date else None

    result = []
    for row in rows:
        row_date = parse_date(row['date'])
        if start and row_date < start:
            continue
        if end and row_date > end:
            continue
        result.append(row)
    return result


def total_value(rows):
    return sum(int(row['value']) for row in rows)


def main(argv):
    """Entry point for command-line execution."""

    start_date = None
    end_date = None
    args = iter(argv)
    for arg in args:
        if arg == '--start':
            start_date = next(args, None)
        elif arg == '--end':
            end_date = next(args, None)

    data = load_data('data.csv')
    filtered = filter_by_date(data, start_date, end_date)
    total = total_value(filtered)

    print(f'Total records: {len(filtered)}')
    print(f'Sum of values: {total}')


if __name__ == '__main__':
    main(sys.argv[1:])
