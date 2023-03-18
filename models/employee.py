from dataclasses import dataclass
from typing import Dict
from .schedule import ScheduleRecord


@dataclass
class Employee:
    name: str
    schedule_records: Dict[str, ScheduleRecord]