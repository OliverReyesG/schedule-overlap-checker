from utils import EmployeeScheduleParser
from reports.schedule_reports import ScheduleOverlapReport

parser = EmployeeScheduleParser()
reporter = ScheduleOverlapReport(parser=parser)
report = reporter.generate("data/test_schedules.txt")
for (names, overlap_count) in report:
    print(names +  ":", overlap_count)