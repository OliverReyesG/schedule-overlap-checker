from abc import ABC
from typing import List, Tuple


class ReportRenderer(ABC):
    def render(report: List[Tuple[str, int]]):
        pass


class ConsoleRenderer(ReportRenderer):
    def render(self, report: List[Tuple[str, int]]):
        for (names, overlap_count) in report:
            print(names +  ":", overlap_count)