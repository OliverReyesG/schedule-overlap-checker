import pytest
from pathlib import Path
from utils import EmployeeScheduleParser


@pytest.fixture
def root_folder():
    return Path(__file__).parents[1]


@pytest.fixture
def target_directory(root_folder):
    return root_folder / "data/test_schedules.txt"


def test_parser_length(target_directory):
    parser = EmployeeScheduleParser()
    employees = parser.parse(target_directory)
    assert len(employees) == 3


def test_parsed_employee_names(target_directory):
    parser = EmployeeScheduleParser()
    employees = parser.parse(target_directory)
    employees[0].name == "RENE"
    employees[1].name == "ASTRID"
    employees[2].name == "ANDRES"