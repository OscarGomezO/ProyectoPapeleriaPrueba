from os import name
from django.urls import path
#from erp.views import *
from erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    #path('uno/', myfirstview, name='vista1'),
    #path('dos/', mysecondview, name='vista2'),
    #path('category/list/', category_list, name='category_list'),  #Para vista basada en función
    path('category/list/', CategoryListView.as_view(), name='category_list'),
]