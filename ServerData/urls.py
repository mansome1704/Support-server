from os import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login, views as authviews
from django.conf import settings
from django.conf.urls.static import static


from . import views 

urlpatterns = [
    path('',views.Home, name = 'Home'),
    
    path('CreateServer/',views.CreateServer, name = 'CreateServer'),
    path('listServer/',views.listServer, name = 'listServer'),
    path('EditServer/<int:id>/',views.EditServer, name = 'EditServer'),
    path('DeleteServer/<int:id>/',views.DeleteServer, name = 'DeleteServer'),
    path('',include('django.contrib.auth.urls')),
    path('show_messages/',views.show_messages, name='show_messages'),
    path('login/',views.login, name='login'),




    path('ShowData/',views.ShowData, name = 'ShowData'),
    #path('ShowProjectTemp/',views.ShowProjectTemp, name = 'ShowProjectTemp'),
    path('ShowServerForm/',views.ShowServerForm, name = 'ShowServerForm'),
    path('Approve/',views.Approve,name='Approve'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


