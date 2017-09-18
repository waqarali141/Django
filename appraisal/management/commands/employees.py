from django.core.management.base import BaseCommand, CommandError

from appraisal.models import Employee

class Command(BaseCommand):
    help = 'Shows Employees list'

    def handle(self, *args, **options):
        employee_list = Employee.objects.all()[:10].values('name', 'type', 'joined_date')
        for employee in employee_list:
            employee['joined_date'] = str(employee['joined_date'])
            self.stdout.write(self.style.SUCCESS("%s" % employee))
