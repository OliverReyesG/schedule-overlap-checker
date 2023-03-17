from dataclasses import dataclass
from typing import List
from .schedule import ScheduleRecord

@dataclass
class Employee:
    name: str
    schedule: List[ScheduleRecord]