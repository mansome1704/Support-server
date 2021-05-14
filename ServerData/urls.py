from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('',views.Home, name = 'Home'),
    
    path('CreateServer/',views.CreateServer, name = 'CreateServer'),
    path('listServer/',views.listServer, name = 'listServer'),
    path('EditServer/<int:id>/',views.EditServer, name = 'EditServer'),
    path('DeleteServer/<int:id>/',views.DeleteServer, name = 'DeleteServer'),


     path('ShowData/',views.ShowData, name = 'ShowData'),
    #path('ShowProjectTemp/',views.ShowProjectTemp, name = 'ShowProjectTemp'),
    path('ShowServerForm/',views.ShowServerForm, name = 'ShowServerForm'),
]


