from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>hello elika</h2>')

def contactus(request):
    return HttpResponse('contactus')

def aboutus(request):
    return HttpResponse('aboutus')