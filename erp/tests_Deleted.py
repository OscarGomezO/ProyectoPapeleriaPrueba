from os import name
import ProyectoPapeleriaPrueba
from django.core.handlers import wsgi
from ProyectoPapeleriaPrueba.wsgi import *
from erp.models import *

#---------*****--//--TABLE--TYPE--\\-------*****----------
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

#---------*****--//--TABLE--CATEGORY--\\-------*****----------
""" obj = Type.objects.filter(name_icontains='pre')
obj = Type.objects.filter(name_endwith='a')
obj = Type.objects.filter()
print(obj) """

""" from ProyectoPapeleriaPrueba.wsgi import *
from erp.models import Category
from erp.models import * """

#-------LISTAR-----(CONSULT)--
#select * from Tabla   --> en Postgresql
""" query = Category.objects.all()
print(query)
 """
""" print(Category.objects.all())

for i in Category.objects.filters():
    print(i) """

#-------INSERT----------------
""" try: 
    t = Category(name = "Bebidas")
    t.name = "Bebidas"
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
    t = Category.objects.get(pk=3)
    t.delete() 
except Exception as e:
    print(e) """

#-------FILTER --------------- El LIke de Postgresql
#obj = Type.objects.filter(name_ic)

#---------*****--//--TABLE--PRODUCT--\\-------*****----------
""" obj = Type.objects.filter(name_icontains='pre')
obj = Type.objects.filter(name_endwith='a')
obj = Type.objects.filter()
print(obj) """

#-------LISTAR-----(CONSULT)--
#select * from Tabla   --> en Postgresql
""" query = Product.objects.all()
print(query) """

""" for i in Product.objects.filters():
    print(i)
 """

#-------INSERT----------------
""" try: 
    t = Product(name = "Yogurt", image=None, pvp=3.50, cate_id= 5)
    t.name = "Yogurt"
    t.image = None
    t.pvp = 3.50
    t.cate_id = 5
    t.save()
except Exception as e:
    print(e)  """

