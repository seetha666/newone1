from django.contrib import admin
from testapp.models import Employee,proxyEmployee,proxyEmployee1
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']

class proxyEmployeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']
    
class proxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']
    
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(proxyEmployee,proxyEmployeeAdmin)
admin.site.register(proxyEmployee1,proxyEmployeeadmin)
