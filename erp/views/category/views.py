from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator #Requerido para el decorator
from django.contrib.auth.decorators import login_required #requerido para el decorator (prueba de login)
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from erp.forms import CategoryForm
from erp.models import Category
from django import forms
from os import name


def category_list(request):  #Lista basada en función
    data = {
        'title' : 'Listado de Categorías',
        'categories' : Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):   #Lista basada en Clase
    model = Category        #Indica cual es el modelo o entidad
    template_name = "category/list.html"    #Cual es la plantilla

    #@method_decorator(login_required)   # Decorador que requiere un login
    @method_decorator(csrf_exempt)       # Decorador que omite la protección de vistas con CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        #Sobreescribe el metodo GET
        #if request.method == 'GET':         # Redirecciona a la vista category_list2
        #    return redirect('erp:category_list2')
        #print(request)
        #return super().dispatch(request, *args, **kwargs)
    #Sobreescribe el metodo POST
    def post(self, request, *args, **kwargs):
        #data = {'name' : 'william'}
        #print(request.POST)
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
            #data['name'] = cat.name
        except Exception as e:
            data['error'] = str(e)      
        return JsonResponse(data)

        

    """ def get_queryset(self):
        #return Category.objects.filter(name__startswith='L') #Sirve para hacer validaciones
        return  Category.objects.all()  #Sirve para hacer validaciones
 """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list') #Me devuelve la ruta que le pase como parametro de la URL es decir, redirecciona 
   
   #Ejemplo de como actua el metodo POST cuando hacemos submit de todos nuestros datos para crear un registro
#    def post(self, request, *args, **kwargs):
#        print(request.POST)
#        form = CategoryForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(self.success_url)
#        self.object = None
#        context = self.get_context_data(**kwargs)   # Recuperamos los valores del diccionario que tiene todos los valores de la vista
#        context['form'] = form
#        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'add'
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list') #Me devuelve la ruta que le pase como parametro de la URL es decir, redirecciona 
    
    #Se utiliza el metodo dispatch para instanciar el objeto y poder hacer correctamente el editar, de lo contrario la instancia se reconoce como crear
    #y en caso de ser el mismo nombre va a salir el mensaje de "registro ya está registrado" y no va realizar el cambio
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        #print(self.object)
        #print(self.get_object) #obtine la instancia del objeto actual
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'edit'
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context
    
    
    

