from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import ServerData

class ServerForm(ModelForm):
    class Meta:
        model = ServerData
        fields = '__all__'
        






