from django.shortcuts import render
from django.http import HttpResponse

def ragada_app(request):
    return render(request, 'homepage.html')