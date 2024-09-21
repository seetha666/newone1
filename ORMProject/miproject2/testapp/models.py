from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        qs=super().get_queryset().order_by("eno")
        return qs
    def get_sal_range(self,min_sal,max_sal):
        qs1=super().get_queryset().filter(esal__range=(min_sal,max_sal))
        return qs1
        
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eadd=models.CharField(max_length=250)
    objects=CustomManager()
