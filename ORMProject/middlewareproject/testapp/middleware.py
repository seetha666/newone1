from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print("init method execution.......")
        self.get_response=get_response
        
        
    def __call__(self, request):
        print("processing request")
        response=self.get_response(request)
        print("post processing")
        return render(request,)
    

class AppMaintainceMiddleware(object):
    def __init__(self,request):
        pass
    
    def __call__(self, request):
        return HttpResponse('<h1>currently application is under maintaince please try after two days </h1>')
        