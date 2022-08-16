from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contactme(request):
    return render(request, 'contactme.html')

def readme(request):
    return render(request, 'readme.html')

def aboutme(request):
    return render(request, 'aboutme.html')