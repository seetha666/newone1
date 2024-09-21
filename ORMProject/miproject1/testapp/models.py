from django.db import models
class ContactInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=250)
    class Meta:
        abstract=True

class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()
    
class Teacher(ContactInfo):
    subject=models.CharField(max_length=25)
    salary=models.FloatField()
    
    
class ContactInfo1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=250)

class Student1(ContactInfo1):
    rollno=models.IntegerField()
    marks=models.IntegerField()
    
class Teacher1(ContactInfo1):
    subject=models.CharField(max_length=25)
    salary=models.FloatField()
    
    
class Person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    
class Employee1(Person):
    eno=models.IntegerField()
    esal=models.FloatField()
print(type(Employee1))
class Manager(Employee1):
    exp=models.IntegerField()
    team_size=models.IntegerField()

class Parant1(models.Model):
    f1=models.CharField(max_length=50)
    f2=models.CharField(max_length=50)
    
class Parant2(models.Model):
    f3=models.CharField(max_length=50,primary_key=True)
    f4=models.CharField(max_length=50)
    
class Child1(Parant1,Parant2):
    f5=models.CharField(max_length=50)
    f6=models.CharField(max_length=50)
    


