from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        print("init method execution.......")
        self.get_response=get_response
        
        
    def __call__(self, request):
        response=self.get_response(request)
        return response
    
    def process_exception(self,request,exception):
        return HttpResponse(f"<h1>current we are facing some technical problem "
                            f"please try after some  timethe raised exception is:"
           f" {exception.__class__.__name__}  <br>the exception message is:{exception}</br>  </h1>")
