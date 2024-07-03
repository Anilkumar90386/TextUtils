from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse('Home<a href="/about">Go to about</a>')
def about(request):
    return HttpResponse('About<a href="/">Go to Home</a>')
