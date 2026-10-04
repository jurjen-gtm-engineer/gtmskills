#!/usr/bin/env python3
"""Build the free owned local table from a Google Maps export.

Own the data once; stop renting each lookup. This indexes a Google-Maps business
dump into a SQLite table keyed on normalized-name + zip, carrying domain + phone +
address, the small-business tail and the phone that pins geography.

Build the export with your own Google Maps scrape, for example with the list-building
skills in coldoutboundskills by Growth Engine X. Do not redistribute data files you
bought or were given.

Usage:
  python3 build_owned_table.py --input google_maps_export.csv --db data/owned.sqlite \
      [--name-col name] [--zip-col zip] [--domain-col website] \
      [--phone-col phone] [--address-col address]
"""
from __future__ import annotations

import argparse
import csv
import os
import sqlite3

from sources import normalize_name, registrable_domain


def pick(row, *candidates):
    for c in candidates:
        if c and c in row and (row[c] or "").strip():
            return row[c].strip()
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--db", required=True)
    ap.add_argument("--name-col")
    ap.add_argument("--zip-col")
    ap.add_argument("--domain-col")
    ap.add_argument("--phone-col")
    ap.add_argument("--address-col")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.db) or ".", exist_ok=True)
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS businesses (
            name_key TEXT, zip TEXT, domain TEXT, phone TEXT, address TEXT
        )""")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_namekey ON businesses(name_key)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_namezip ON businesses(name_key, zip)")
    conn.commit()

    n, kept = 0, 0
    with open(args.input, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        batch = []
        for row in reader:
            n += 1
            name = pick(row, args.name_col, "name", "Name", "company", "title")
            website = pick(row, args.domain_col, "website", "Website", "url", "domain")
            domain = registrable_domain(website)
            if not name or not domain:
                continue
            zip_code = pick(row, args.zip_col, "zip", "Zip", "postal_code", "zipcode")
            phone = pick(row, args.phone_col, "phone", "Phone", "phone_number")
            address = pick(row, args.address_col, "address", "Address", "full_address")
            batch.append((normalize_name(name), zip_code, domain, phone, address))
            kept += 1
            if len(batch) >= 5000:
                cur.executemany("INSERT INTO businesses VALUES (?,?,?,?,?)", batch)
                conn.commit()
                batch = []
        if batch:
            cur.executemany("INSERT INTO businesses VALUES (?,?,?,?,?)", batch)
            conn.commit()

    print(f"Read {n} rows, indexed {kept} with a name + resolvable domain -> {args.db}")
    conn.close()


if __name__ == "__main__":
    main()
