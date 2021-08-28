from os import name
from django.urls import path
from erp.views_Deleted import *
from erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('uno/', myfirstview, name='vista1'),
    #path('dos/', mysecondview, name='vista2'),
    #path('category/list/', category_list, name='category_list'),  #Para vista basada en función
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'), #<Int:pk> es un paramatero adicional que va a ser la PK
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'), #<Int:pk> es un paramatero adicional que va a ser la PK
    
]