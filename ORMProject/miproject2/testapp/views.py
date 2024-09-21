from django.shortcuts import render
from testapp.models import Employee
def display_view(request):
    emp_list=Employee.objects.get_sal_range(1000,3000)
    # here view level we doing ascending or i want do logic model level 
    # then we have to write logic in model class by using model manager
    return render(request,'testapp/index.html',{'emp_list':emp_list})