from django.http import HttpResponse
from django.shortcuts import render
def text(request):
    return render(request,'ind.html')