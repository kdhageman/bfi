# BFI
Converts a [BFI Excel file](https://ufm.dk/en/research-and-innovation/statistics-and-analyses/bibliometric-research-indicator/bfi-lists "Page with BFI files") (`.xlsx`) to a sqlite3 database (`.db`).

## Usage
```
usage: bfi.py [-h] [--in INFILE] [--out OUTFILE]

Convert the Danish BFI form Excel file to a sqlite3 database

optional arguments:
  -h, --help     show this help message and exit
  --in INFILE    Path to .xlsx input file
  --out OUTFILE  Path to .db output file
```

## Requirements
Following is needed:
- `Python 3`

Install dependencies as follows:
```
pip install -r requirements
``` 