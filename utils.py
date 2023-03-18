from abc import ABC
from typing import List
import re
from models.employee import Employee
from models.schedule import ScheduleRecord


class FileParser(ABC):
    def __read_file(self, path):
        pass

    def parse(self, path):
        pass


class EmployeeScheduleParser(FileParser):
    def __init__(self):
        pass

    
    def __read_file(self, path: str) -> List[str]:
        with open(path) as f:
            return f.readlines()


    def parse(self, path: str) -> List[Employee]:
        employees = []
        file = self.__read_file(path)
        name_pattern = r'([A-Z]+)='
        schedule_record_pattern = r'(([A-Z]{2})([\d]{2}:[\d]{2})\s*-\s*([\d]{2}:[\d]{2}))'
        for line in file:
            employee_name = re.search(name_pattern, line).group(1)
            raw_schedule_records = re.findall(schedule_record_pattern, line)
            schedule_records = {f"{day}": ScheduleRecord(arrival_time=arrival_time, leave_time=leave_time) for (match, day, arrival_time, leave_time) in raw_schedule_records}
            employees.append(Employee(name=employee_name, schedule_records=schedule_records))
        return employees


def check_time_overlap(record1: ScheduleRecord, record2: ScheduleRecord):
    if record1.arrival_time >= record2.arrival_time and record1.leave_time <= record2.leave_time:
        return True
    return False


def count_schedule_overlap(schedule1: dict, schedule2: dict):
    overlap_count = 0
    for key in schedule1.keys():
        if key in schedule2.keys() and check_time_overlap(schedule1[key], schedule2[key]):
            overlap_count += 1
    return overlap_count