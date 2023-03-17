from dataclasses import dataclass

@dataclass
class ScheduleRecord:
    day: str
    arrival_time: str
    leave_time: str