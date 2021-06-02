import os
import datetime
from typing_extensions import Protocol


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ServerData.models import ServerData
# from UserData.models import User
from ServerData.forms import ServerForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "login.html", {"form": form, "msg" : msg})

@login_required(login_url="/login/")
def Home(request):
    return render(request,'index.html')

@login_required(login_url="/login/")
def ShowData(request):
    return render(request,'Showdata.html')


@login_required(login_url="/login/")
def listServer(request):

    # CurrentUser = request.user
    Server = ServerData.objects.all()
    data = {'AllServer' :  Server}

    return render(request,'Showdata.html',data)
    meassages.set_level(request,messages.DEBUB)
    
    meassages.debug(request,'Save Success')
    meassages.info(request,'Save Success')
    meassages.success(request,'Save Seccess')
    meassages.warning('Save Success')
    meassages.error('Save Success')




@login_required(login_url="/login/")
def EditServer(request,id):
    Server = ServerData.objects.get(id = id)
    if request.method == 'POST':
        form =  ServerForm(request.POST or None, request.FILES , instance = Server)
        if form.is_valid():
            form.save()
            return redirect('/listServer/')
    else:
       MyServerForm  = ServerForm(instance = Server)
       data = {'form' : MyServerForm}
       return render(request,'editServer.html',data)


@login_required(login_url="/login/")
def CreateServer(request):    
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            NewServer = form.save(commit=False)
            # NewLeave.Person = request.user
            NewServer.save()
            return redirect('/listServer/')
    else:
        NewServerForm  = ServerForm()
        data = {'form' : NewServerForm}
        return render(request,'EditServer.html',data)


@login_required(login_url="/login/")
def DeleteServer(request,id):    
    Server = ServerData.objects.get(id = id)
    Server.delete()
    return redirect('/listServer/')


# def ShowProjectTemp(request):,
#     return render(request,'temp_proj.html')

@login_required(login_url="/login/")
def ShowServerForm(request):
    form = ServerForm()
    return render(request,'ServerForm.html',{'form':form})







