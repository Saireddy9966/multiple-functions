from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('<h1> This is my fist function in second application</h1>')

def second_app2(request):
    return HttpResponse('<h1> This is my second function in second application</h1>')



