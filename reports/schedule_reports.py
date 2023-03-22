from abc import ABC
from typing import List, Tuple
from utils import FileParser
from models.schedule import ScheduleRecord


class ScheduleReport(ABC):
    def __init__(self, parser: FileParser) -> None:
        self.parser = parser
    
    
    def generate(self, path: str) -> List[Tuple[str, int]]:
        pass


class ScheduleOverlapReport(ScheduleReport):

    def check_time_overlap(self, record1: ScheduleRecord, record2: ScheduleRecord) -> bool:
        if record1.arrival_time >= record2.arrival_time and record1.leave_time <= record2.leave_time:
            return True
        return False


    def count_schedule_overlap(self, schedule1: dict, schedule2: dict) -> int:
        overlap_count = 0
        for key in schedule1.keys():
            if key in schedule2.keys() and self.check_time_overlap(schedule1[key], schedule2[key]):
                overlap_count += 1
        return overlap_count
    
    
    def generate(self, path: str) -> List[Tuple[str, int]]:
        employees = self.parser.parse(path)
        if len(employees) == 0:
            return []
        schedule_overlap_report = []
        for i in range(len(employees) - 1):
            for j in range(i+1, len(employees)):
                names = employees[i].name + "-" + employees[j].name
                overlap_count = self.count_schedule_overlap(employees[i].schedule_records, employees[j].schedule_records)
                schedule_overlap_report.append((names, overlap_count))
        return schedule_overlap_report