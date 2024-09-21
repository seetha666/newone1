from django.shortcuts import render
from django.db.models import Q
from testapp.models import Employee
def retrive_view(request):
    emp_list=Employee.objects.all().order_by('ename')
    print(emp_list)

    print(type(emp_list))
    return render(request,'testapp/index.html',{"emp_list":emp_list})
from django.db.models import Max,Min,Avg,Sum,Count
def agregate_view(request):
    print(request.user)
    max=Employee.objects.all().aggregate(Max('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    avg=Employee.objects.all().aggregate(Avg('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))
    print(max)
    my_dict={'max':max['esal__max'],'min':min['esal__min'],'avg':avg['esal__avg'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)
