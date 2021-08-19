from django.urls import path
from erp.views import *

urlpatterns = {
    path('uno/', myfirstview),
    path('dos/', mysecondview),

}