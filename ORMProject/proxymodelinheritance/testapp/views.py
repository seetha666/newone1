from django.shortcuts import render
from testapp.models import Employee,proxyEmployee,proxyEmployee1

def home_page_view(request):
    name1=request.GET.get('salaryrange')
    if name1=='lessthan5000':
        emp_list=proxyEmployee.objects.all()
    elif name1=='graterthan5000':
        emp_list=Employee.objects.all()
    else:
        emp_list=proxyEmployee1.objects.all()
    
    return render(request,'testapp/index.html',{'emp_list':emp_list})

