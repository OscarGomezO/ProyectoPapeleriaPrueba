from django.http.response import HttpResponse
from django.shortcuts import render
from erp.models import Category, Product

""" # Create your views here.
def myfirstview(request):
    data = {            #Dictionary
        'name' : 'Williams',
        'categories' : Category.objects.all()
    }
    #return HttpResponse("Hola, Esta es la primera Vista")
    return render(request, 'home.html', data)   #rende permite interactuar con una plantilla enviandole ciertos parametros, "index.html" es el archivo html plantilla, data es un parametro opcional;
 """
def myfirstview(request):
    data = {            #Dictionary
        'name' : 'Williams',
        'categories' : Category.objects.all()
    }
    #return HttpResponse("Hola, Esta es la primera Vista")
    return render(request, 'index2.html', data)

def mysecondview(request):  #Vista prueba herencia
    data = {
        'name' : 'Lona',
        'categories' : Category.objects.all(),
        'products' : Product.objects.all()

    }
    #return HttpResponse("Hola, Esta es la segunda Vista")
    return render(request, 'second.html', data)


