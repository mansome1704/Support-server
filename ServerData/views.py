import os
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ServerData.models import ServerData
# from UserData.models import User
from ServerData.forms import ServerForm



def Home(request):
    return render(request,'base.html')


def ShowData(request):
    return render(request,'Showdata.html')


@login_required
def listServer(request):
    # CurrentUser = request.user
    Server = ServerData.objects.all()
    data = {'AllServer' :  Server}
    return render(request,'Showdata.html',data)


@login_required
def EditServer(request,id):
    Server = ServerData.objects.get(id = id)
    if request.method == 'POST':
        form =  ServerForm(request.POST or None, instance = Server)
        if form.is_valid():
            form.save()
            return redirect('/listServer/')
    else:
       MyServerForm  = ServerForm(instance = Server)
       data = {'form' : MyServerForm}
       return render(request,'editServer.html',data)


@login_required
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


login_required
def DeleteServer(request,id):    
    Server = ServerData.objects.get(id = id)
    Server.delete()
    return redirect('/listServer/')


# def ShowProjectTemp(request):,
#     return render(request,'temp_proj.html')


def ShowServerForm(request):
    form = ServerForm()
    return render(request,'ServerForm.html',{'form':form})



