 #Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def myapp_message(request):
    return HttpResponse("This is MyApp message page! ")