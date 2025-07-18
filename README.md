# Sample Totalizer App

This repository contains a minimal Python script that demonstrates how to
filter records by date and compute totals. The example data is stored in
`data.csv`.

## Running the example

1. Ensure you have Python 3 installed.
2. Run `python app.py` with optional `--start` and `--end` parameters
   to filter the data by date range.

```
# Show totals for all records
python app.py

# Filter from 2024-02-01 onward
python app.py --start 2024-02-01

# Filter between two dates
python app.py --start 2024-01-10 --end 2024-03-01
```

The script outputs the number of filtered records and the sum of the
`value` column.
