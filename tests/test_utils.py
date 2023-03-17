import pytest
from pathlib import Path
from utils import EmployeeScheduleParser

def test_employee_schedule_parser():
    employee_schedule_parser = EmployeeScheduleParser()
    root_folder =  Path(__file__).parents[1]
    target_directory = root_folder / "data/test_schedules.txt"
    employes = employee_schedule_parser.parse(target_directory)

    assert employes[0].name == "RENE"
    assert employes[0].schedule[0].day == "MO"
    assert employes[0].schedule[0].arrival_time == "10:00"
    assert employes[0].schedule[0].leave_time == "12:00"

    assert employes[0].schedule[4].arrival_time == "20:00"
    assert employes[0].schedule[4].leave_time == "21:00"