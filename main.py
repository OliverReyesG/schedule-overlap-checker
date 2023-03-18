from utils import EmployeeScheduleParser, count_schedule_overlap
from models.employee import Employee
from models.schedule import ScheduleRecord

parser = EmployeeScheduleParser()

employees = parser.parse("data/test_schedules.txt")

for i in range(len(employees) - 1):
    for j in range(i+1, len(employees)):
        names = employees[i].name + "-" + employees[j].name
        print(names+":", count_schedule_overlap(employees[i].schedule_records, employees[j].schedule_records))