from django.core.management.base import BaseCommand, CommandError

from appraisal.models import Employee

class Command(BaseCommand):
    help = 'Shows Employees list'

    def handle(self, *args, **options):
        employee_list = Employee.objects.all()[:10]

        for employee in employee_list:
            dict = {'Name': employee.name,
                    'Position': employee.get_type_display(),
                    'joining Date': str(employee.joined_date.date())}
            if employee.reporting_to:
                dict['Reporting To'] = employee.reporting_to.name
            self.stdout.write(self.style.SUCCESS("%s" % dict))