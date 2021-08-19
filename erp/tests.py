from django.test import TestCase

# Create your tests here.
from ProyectoPapeleriaPrueba.wsgi import *
from erp.models import Categoria

#-------LISTAR-----(CONSULT)--
#select * from Tabla   --> en Postgresql
"""query = Categoria.objects.all()
print(query)"""

#-------INSERT----------------

"""t = Categoria()
t.name = "Central Park"
t.save()"""

#-------EDIT------------------
"""try:
    t = Categoria.objects.get(pk=3)
    print(t.name)
    t.name = 'EE.UU'
    t.save()
except Exception as e:
    print(e)"""

#-------DELETE----------------
""" t = Categoria.objects.get(pk=1)
t.delete() """

#-------FILTER --------------- El LIke de Postgresql
#obj = Type.objects.filter(name_ic)