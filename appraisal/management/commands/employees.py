# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from appraisal.models import Employee


class Command(BaseCommand):
    help = 'Shows Employees list'
    users = [('hamza', '1234qwer'), ('badr', '1234qwer'), ('badr1', '1234qwer'), ('badr2', '1234qwer'),
             ('badr3', '1234qwer'), ('zunair', '1234qwer'), ('zunair1', '1234qwer'), ('zunair2', '1234qwer'),
             ('zunair3', '1234qwer'), ('waqar', '1234qwer'), ('waqar1', '1234qwer'), ('waqar2', '1234qwer')
             ]
    employees = {'hamza': ['waqar', 'badr', 'zunair'],
                 'badr': ['badr1', 'badr2', 'badr3'],
                 'zunair': ['zunair1', 'zunair2', 'zunair3'],
                 'waqar': ['waqar1', 'waqar2']}

    def handle(self, *args, **options):
        for (username, password) in self.users:
            user_object = User.objects.create_user(username=username, password=password)
            if username == 'waqar':
                user_object.is_superuser = True
                user_object.is_active = True
                user_object.is_staff = True
                user_object.save()
            self.stdout.write(self.style.SUCCESS("Created user with username: %s" % user_object.username))

        mg_user = User.objects.get(username='hamza')
        mg_employee_object = Employee.create_employee(mg_user, 'hamza', 'mg', )
        mg_employee_object.save()
        self.stdout.write(self.style.SUCCESS("Created Employee with username: %s" % mg_employee_object.name))
        for employee in self.employees['hamza']:
            gm_user = User.objects.get(username=employee)
            gm_employee_object = Employee.create_employee(gm_user, employee, 'gm', mg_employee_object)
            gm_employee_object.save()
            self.stdout.write(self.style.SUCCESS("Created Employee with username: %s" % gm_employee_object.name))
            for sf_employee in self.employees[employee]:
                sf_user = User.objects.get(username=sf_employee)
                sf_employee_object = Employee.create_employee(sf_user, sf_employee, 'sf', gm_employee_object)
                sf_employee_object.save()
                self.stdout.write(self.style.SUCCESS("Created Employee with username: %s" % sf_employee_object.name))
