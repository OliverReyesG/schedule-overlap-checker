import pytest
from pathlib import Path
from utils import EmployeeScheduleParser
from reports.schedule_reports import ScheduleOverlapReport
from reports.report_renderer import ConsoleRenderer

@pytest.fixture
def root_folder():
    return Path(__file__).parents[1]


@pytest.fixture
def target_directory(root_folder):
    return root_folder / "data/test_schedules.txt"


@pytest.fixture
def report(target_directory):
    report_generator = ScheduleOverlapReport(EmployeeScheduleParser())
    report = report_generator.generate(target_directory)
    return report


def test_overlap_report(report, capsys):
    report_renderer = ConsoleRenderer()
    report_renderer.render(report)
    out, err = capsys.readouterr()
    assert out == "RENE-ASTRID: 2\nRENE-ANDRES: 2\nASTRID-ANDRES: 3\n"