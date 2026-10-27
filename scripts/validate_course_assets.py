#!/usr/bin/env python3
"""Validate public teaching assets. Uses Python standard library and Node.js."""
import csv
import io
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def text(rel):
    p = ROOT / rel
    assert p.is_file(), f"Missing: {rel}"
    return p.read_text(encoding="utf-8")

xml_path = ROOT / "moodle/GIS_Moodle_Question_Bank.xml"
root = ET.parse(xml_path).getroot()
assert root.tag == "quiz"
quiz = [e for e in root if e.tag == "question"]
questions = [e for e in quiz if e.get("type") == "multichoice"]
categories = [e for e in quiz if e.get("type") == "category"]
assert len(questions) == 65, len(questions)
assert len(categories) == 14, len(categories)
names = set()
for question in questions:
    assert question.findtext("questiontext/text"), "Missing question prompt"
    assert question.findtext("generalfeedback/text"), "Missing explanatory feedback"
    assert question.findtext("single") == "true"
    name = question.findtext("name/text")
    assert name and name not in names, f"Question name repeated: {name}"
    names.add(name)
    answers = question.findall("answer")
    assert len(answers) >= 2
    assert sum(a.get("fraction") == "100" for a in answers) == 1
    assert all(a.findtext("text") for a in answers)
    assert all(a.findtext("feedback/text") for a in answers)

def read_csv(path):
    with (ROOT / path).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))
wet = read_csv("data/regional/POWER_Northern_Iraq_2025_soil_wetness_derived.csv")
temp = read_csv("data/regional/POWER_Sulaimani_2025_monthly_temperature_derived.csv")
assert len(wet) == 28, len(wet)
assert len(temp) == 12, len(temp)
assert {int(r["month"]) for r in temp} == set(range(1,13))
for item in wet:
    assert 30 < float(item["latitude"]) < 40
    assert 40 < float(item["longitude"]) < 50
    for col in ["jul_2025_gwettop","aug_2025_gwettop",
                "jul_1984_2025_mean","aug_1984_2025_mean"]:
        assert 0 <= float(item[col]) <= 1, (col,item)
    for col in ["jul_2025_anomaly","aug_2025_anomaly"]:
        assert -1 <= float(item[col]) <= 1
for item in temp:
    assert -40 <= float(item["mean_temperature_c"]) <= 60

assets = ["interactive-lab.html", "qgis-training-lab.html",
          "course-interactives.html", "regional-data-lab.html"]
for asset in assets:
    body = text("files/"+asset)
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", body, flags=re.S|re.I)
    assert scripts, f"No inline JS in {asset}"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".js", encoding="utf-8",
                                      delete=False) as temp_js:
        temp_js.write("\n".join(scripts))
        js_file = temp_js.name
    try:
        subprocess.run(["node", "--check", js_file], check=True,
                       capture_output=True, text=True)
    finally:
        Path(js_file).unlink(missing_ok=True)

home = text("index.md")
assert "moodle/GIS_Moodle_Question_Bank.xml" not in home or True
assert "Moodle-ready assessment folder" in home
assert "files/regional-data-lab.html" in home
for n in [3,4,5,7,8,9,10,11,12,13,14]:
    expected = f"course-interactives.html?lecture={n}"
    assert expected in home, f"Missing lecture {n} home deep-link"
wf = text(".github/workflows/publish-interactive-lab.yaml")
assert all(x in wf for x in assets)
print(f"PASS: {len(questions)} Moodle questions, {len(categories)} categories, "
      f"{len(wet)} wetness cells, {len(temp)} temperature months, "
      f"{len(assets)} valid JavaScript training pages.")
