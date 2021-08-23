from os import name
from erp.models import Category, Product
from django.shortcuts import render 
from django.views.generic import ListView

def category_list(request):  #Lista basada en función
    data = {
        'title' : 'Listado de Categorías',
        'categories' : Category.objects.all(),
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):   #Lista basada en Clase
    model = Category        #Indica cual es el modelo o entidad
    template_name = "category/list.html"    #Cual es la plantilla

    def get_queryset(self):
        return Category.objects.filter(name__startswith='L') #Sirve para hacer validaciones
        #return Product.objects.all()  #Sirve para hacer validaciones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context