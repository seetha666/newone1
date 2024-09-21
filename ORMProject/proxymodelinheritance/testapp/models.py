from django.db import models

class CustomManager1(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(esal__gte=5000)
    
class CustomManager3(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by('eno')
    
    
class CustomManager2(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(esal__lte=5000)

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eadd=models.CharField(max_length=250)
    objects=CustomManager1()
   
class proxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True
        
class proxyEmployee1(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True
