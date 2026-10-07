"""Ejecuta unittest y conserva reportes JSON y JUnit XML incluso ante un fallo."""
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cases = []

    def startTest(self, test):
        self.case_started = time.perf_counter()
        super().startTest(test)

    def stopTest(self, test):
        self.cases.append({"name": test.id(), "seconds": time.perf_counter() - self.case_started})
        super().stopTest(test)


started = time.perf_counter()
suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
result = unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run(suite)
elapsed = time.perf_counter() - started
reports = ROOT / "reports"
reports.mkdir(exist_ok=True)
summary = {
    "scope": "Contratos del HTML académico y HTTP local; sin backend ni servicios externos",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "tests": result.testsRun,
    "failures": len(result.failures),
    "errors": len(result.errors),
    "skipped": len(result.skipped),
    "elapsed_seconds": elapsed,
    "successful": result.wasSuccessful(),
    "cases": result.cases,
}
(reports / "landing-tests.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
xml = ET.Element("testsuite", name="AcademicLanding", tests=str(result.testsRun),
                 failures=str(len(result.failures)), errors=str(len(result.errors)),
                 skipped=str(len(result.skipped)), time=f"{elapsed:.6f}")
for recorded in result.cases:
    case = ET.SubElement(xml, "testcase", name=recorded["name"], time=f'{recorded["seconds"]:.6f}')
    for kind, items in (("failure", result.failures), ("error", result.errors)):
        for test, message in items:
            if test.id().startswith(recorded["name"]):
                ET.SubElement(case, kind).text = message
    for test, reason in result.skipped:
        if test.id() == recorded["name"]:
            ET.SubElement(case, "skipped", message=reason)
ET.ElementTree(xml).write(reports / "landing-junit.xml", encoding="utf-8", xml_declaration=True)
sys.exit(0 if result.wasSuccessful() else 1)
