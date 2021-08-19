""" from os import name
import ProyectoPapeleriaPrueba
from django.core.handlers import wsgi
from ProyectoPapeleriaPrueba.wsgi import *
from erp.models import Type """

#--------------------------TABLA--TYPE-------------------
#-------LISTAR-----(CONSULT)--
#select * from Tabla   --> en Postgresql
""" query = Type.objects.all()
print(query) """

#-------INSERT----------------
""" try: 
    t = Type(name = "Hollywood")
    t.name = "Hollywood"
    t.save()
except Exception as e:
    print(e) """

#-------EDIT------------------
""" try:
    t = Type.objects.get(pk=1)
    print(t.name)
    t.name = 'Accionista001'
    t.save()
except Exception as e:
    print(e) """

#-------DELETE----------------
""" t = Type.objects.get(pk=1)
t.delete() """

#-------//-------------CONSULTs 2-------------\\-----------
""" obj = Type.objects.filter(name_icontains='pre')
obj = Type.objects.filter(name_endwith='a')
obj = Type.objects.filter()
print(obj) """

from ProyectoPapeleriaPrueba.wsgi import *
from erp.models import Category

#-------LISTAR-----(CONSULT)--
#select * from Tabla   --> en Postgresql
query = Category.objects.all()
print(query)

#-------INSERT----------------
""" try: 
    t = Category(name = "Empire State")
    t.name = "Empire State"
    t.save()
except Exception as e:
    print(e)  """


#-------EDIT------------------
""" try:
    t = Category.objects.get(pk=3)
    print(t.name)
    t.name = 'EE.UU'
    t.save()
except Exception as e:
    print(e) """

#-------DELETE----------------
""" try:
    t = Category.objects.get(pk=4)
    t.delete() 
except Exception as e:
    print(e) """

#-------FILTER --------------- El LIke de Postgresql
#obj = Type.objects.filter(name_ic)