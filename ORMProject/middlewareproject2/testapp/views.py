from django.shortcuts import render
from django.http import HttpResponse
def home_page_view(request):
    print(10/0)
    return HttpResponse("<h3>Hello this is from form view function</h3>")
