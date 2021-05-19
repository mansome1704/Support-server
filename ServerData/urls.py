from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authviews

from . import views 

urlpatterns = [
    path('',views.Home, name = 'Home'),
    
    path('CreateServer/',views.CreateServer, name = 'CreateServer'),
    path('listServer/',views.listServer, name = 'listServer'),
    path('EditServer/<int:id>/',views.EditServer, name = 'EditServer'),
    path('DeleteServer/<int:id>/',views.DeleteServer, name = 'DeleteServer'),
    path('account/',include('django.contrib.auth.urls')),


    path('login/',authviews.LoginView.as_view(), name = 'Login'),
	path('logout/',authviews.LogoutView.as_view(), name = 'Logout'),

    path('ShowData/',views.ShowData, name = 'ShowData'),
    #path('ShowProjectTemp/',views.ShowProjectTemp, name = 'ShowProjectTemp'),
    path('ShowServerForm/',views.ShowServerForm, name = 'ShowServerForm'),
]


