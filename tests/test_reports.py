import pytest
from pathlib import Path
from utils import EmployeeScheduleParser
from reports.schedule_reports import ScheduleOverlapReport

@pytest.fixture
def root_folder():
    return Path(__file__).parents[1]


@pytest.fixture
def target_directory(root_folder):
    return root_folder / "data/test_schedules.txt"

@pytest.fixture
def report(target_directory):
    parser = EmployeeScheduleParser()
    reporter = ScheduleOverlapReport(parser=parser)
    report = reporter.generate(target_directory)
    return report


def test_overlap_report(report):
    assert len(report) == 3


def test_report_types(report):
    for report_entry in report:
        assert isinstance(report_entry[0], str)
        assert isinstance(report_entry[1], int)