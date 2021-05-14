from django.db import models
from django.forms import ModelForm

from .models import ServerData

class ServerForm(ModelForm):
    class Meta:
        model = ServerData
        fields = '__all__'
        # fields = ['Date', 'OS', 'Rom','Ram', 'Servics']
