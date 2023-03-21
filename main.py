from utils import EmployeeScheduleParser
from reports.schedule_reports import ScheduleOverlapReport
from reports.report_renderer import ConsoleRenderer


report_generator = ScheduleOverlapReport(EmployeeScheduleParser())
report_renderer = ConsoleRenderer()
report = report_generator.generate("data/test_schedules.txt")
report_renderer.render(report)
