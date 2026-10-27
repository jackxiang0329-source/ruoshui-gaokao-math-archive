#!/usr/bin/env python3
"""Retypeset only historical Gaokao examinations from 1952 through 1999."""
import argparse
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def historical_years(coverage):
    return sorted((y for y in coverage if y.isdigit() and 1952 <= int(y) <= 1999), reverse=True)

def select_year(requested="", root=ROOT):
    years = json.loads((root / "source-coverage.json").read_text(encoding="utf-8"))["years"]
    permitted = historical_years(years)
    if requested:
        if requested not in permitted:
            raise ValueError("Only 1952-1999 can be retypeset. Preserve the original 2000+ layouts.")
        return requested
    return next((year for year in permitted
        if not (root / "annual" / ("ruoshui-gaokao-" + year + ".pdf")).is_file()
        and not (root / "blocked" / (year + ".json")).is_file()), "")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", default="")
    print(select_year(parser.parse_args().year))
