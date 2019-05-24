from django.shortcuts import render
from django.http import HttpResponse;
from datetime import datetime

def go(request):
    return render(request,'home.html',{"n":str(datetime.now())});

