import argparse
import sqlite3
import xlrd

drop_table_qry = """
DROP TABLE IF EXISTS bfi
"""

create_table_qry = """
CREATE TABLE bfi (
  faggruppe_nr INT,
  faggruppe_navn TEXT,
  bfi_nr INT,
  issn TEXT,
  kanal TEXT,
  title TEXT,
  niveau INT  
)
"""

insert_qry = """
INSERT INTO bfi 
VALUES(?,?,?,?,?,?,?)
"""


class Record:
    def __init__(self, row):
        self.faggruppe_nr = int(row[0].value)
        self.faggruppe_navn = row[1].value
        self.bfi_nr = int(row[2].value)
        self.issn = row[3].value
        self.kanal = row[4].value
        self.title = row[5].value
        self.niveau = int(row[6].value)

    def as_tuple(self):
        return tuple([
            self.faggruppe_nr,
            self.faggruppe_navn,
            self.bfi_nr,
            self.issn,
            self.kanal,
            self.title,
            self.niveau
        ])


def main(args):
    conn = sqlite3.connect(args.outfile)
    c = conn.cursor()
    c.execute(drop_table_qry)
    c.execute(create_table_qry)

    workbook = xlrd.open_workbook(args.infile)
    sheet = workbook.sheet_by_index(0)

    records = []
    for i, row in enumerate(sheet.get_rows()):
        if i == 0:
            continue
        records += [Record(row).as_tuple()]

    c.executemany(insert_qry, records)
    conn.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert the Danish BFI form Excel file to a sqlite3 database")
    parser.add_argument(
        "--in",
        type=str,
        dest='infile',
        default="bfi.xlsx",
        help="Path to .xlsx input file"
    )
    parser.add_argument(
        "--out",
        type=str,
        dest='outfile',
        default="bfi.db",
        help="Path to .db output file"
    )
    args = parser.parse_args()

    main(args)
