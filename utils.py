from abc import ABC
from typing import List
import re
from models.employee import Employee
from models.schedule import ScheduleRecord


class FileParser(ABC):
    def __read_file(self, path: str):
        pass

    def parse(self, path: str) -> List[Employee]:
        pass


class EmployeeScheduleParser(FileParser):
    def __read_file(self, path: str) -> List[str]:
        try:
            with open(path) as f:
                return f.readlines()
        except:
            return []


    def parse(self, path: str) -> List[Employee]:
        employees = []
        file = self.__read_file(path)
        if len(file) == 0:
            return []
        name_pattern = r'([A-Z]+)='
        schedule_record_pattern = r'(([A-Z]{2})([\d]{2}:[\d]{2})\s*-\s*([\d]{2}:[\d]{2}))'
        for line in file:
            employee_name = re.search(name_pattern, line).group(1)
            raw_schedule_records = re.findall(schedule_record_pattern, line)
            schedule_records = {f"{day}": ScheduleRecord(arrival_time=arrival_time, leave_time=leave_time) for (match, day, arrival_time, leave_time) in raw_schedule_records}
            employees.append(Employee(name=employee_name, schedule_records=schedule_records))
        return employees