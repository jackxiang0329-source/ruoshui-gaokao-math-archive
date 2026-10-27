import argparse,json
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("--year",default="")
a=p.parse_args()
root=Path(__file__).parent
years=json.loads((root/"source-coverage.json").read_text())["years"]
if a.year and a.year not in years: raise SystemExit("Unknown year")
print(a.year or next((y for y in years if not (root/"annual"/("ruoshui-gaokao-"+y+".pdf")).is_file()),""))
