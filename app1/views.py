from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app1(request):
    return HttpResponse('<h1>This is my first application first program</h1>')

def second_app1(request):
    return HttpResponse('<h1>This is my first application second program</h1>')