import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from signoff_summary_ml import parse_timing_report, parse_area_report

def test_real_timing_report():
    path = os.path.join('reports', 'pt_report.txt')
    slack, violations = parse_timing_report(path)
    assert isinstance(slack, float), "Slack should be a float"
    assert isinstance(violations, int), "Violations should be an integer"
    assert violations > 0, "Should detect at least one violation"

def test_real_area_report():
    path = os.path.join('reports', 'area_report.txt')
    area = parse_area_report(path)
    assert isinstance(area, float), "Area should be a float"
    assert area > 0, "Area should be positive"