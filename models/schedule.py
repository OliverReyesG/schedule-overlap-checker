from dataclasses import dataclass
from typing import List

@dataclass
class ScheduleRecord:
    day: str
    arrival_time: str
    leave_time: str