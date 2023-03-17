import pytest
from pathlib import Path
from utils import EmployeeScheduleParser, check_day_overlap, check_time_overlap, count_overlap

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


def test_check_day_overlap(target_directory):
    parser = EmployeeScheduleParser()
    employees = parser.parse(target_directory)
    assert check_day_overlap(employees[0].schedule[0], employees[1].schedule[0]) == True
    assert check_day_overlap(employees[1].schedule[1], employees[2].schedule[2]) == False


def test_check_time_overlap(target_directory):
    parser = EmployeeScheduleParser()
    employees = parser.parse(target_directory)
    assert check_time_overlap(employees[0].schedule[0], employees[1].schedule[0]) == True
    assert check_time_overlap(employees[2].schedule[0], employees[0].schedule[2]) == False