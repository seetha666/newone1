from django.shortcuts import render
from django.http import HttpResponse
def welcome_view(request):
    print("viwe function is executed")
    return HttpResponse('<h1>custom middleware demo</h1>')
