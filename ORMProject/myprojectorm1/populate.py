import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myprojectorm1.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        fno=randint(100,200)
        fname=faker.name()
        fsal=randint(1000,10000)
        fadd=faker.city()
        emprecord=Employee.objects.get_or_create(
            eno=fno,
            ename=fname,
            esal=fsal,
            eadd=fadd
            )
    
n=int(input("Enter the no of records"))
populate(n)
print(f'{n} records created succussfully ')
