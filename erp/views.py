from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    data = {            #Dictionary
        'name' : 'Williams'
    }
    return HttpResponse("Hola, esta es mi primera Vista")

def mysecondview(request):
    data = {
        'name' : 'Lona'
    }
    return HttpResponse('Hola, esta es mi segunda vista')