from django.shortcuts import render
from django.http import HttpResponse
def home_page_view(request):
    print("this line is printed by view function")
    return HttpResponse("<h1>Hello this is from view function</h1>")
