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
            schedule = [ScheduleRecord(day=record[1], arrival_time=record[2], leave_time=record[3]) for record in raw_schedule_records]
            employees.append(Employee(name=employee_name, schedule=schedule))
        return employees
