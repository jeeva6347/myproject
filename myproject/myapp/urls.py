from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
path('',views.create,name="create"),
path('edit/<int:id>/',views.edit,name="edit"),
path('delete/<int:id>/',views.delete,name="delete"),


   
   
]
