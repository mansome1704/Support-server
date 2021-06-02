import datetime
from django.db import models

# Create your models here.
OS = [
    ('Window', 'Window'),
    ('Linux', 'Linux'),
       
]

Rom = [
    ('40 GB', '40 GB'),
    ('80 GB', '80 GB'),
       
]

Servics = [
    ('Web Server','Web Server'),
    ('App Server','App Server'),
    ('Database Server','Database Server'),
]

Ram = [
    ('4 GB','4 GB'),
    ('8 GB','8 GB'),
    
]

class ServerData(models.Model): 
    class Meta:
        verbose_name_plural = "ข้อมูลเซิร์ฟ[ServerData]"   
    Date = models.DateField(default=datetime.date.today, verbose_name= "วันที่")
    OS =models.CharField(max_length = 10, choices = OS, default = 'Window')
    Rom = models.CharField(max_length = 10, choices = Rom, default = '40 GB')
    Ram = models.CharField(max_length = 10, choices = Ram, default = '4 GB')
    Servics = models.CharField(max_length = 20, choices = Servics, default = 'Web Server')
    DomainName= models.CharField(max_length=255,default="-" ,verbose_name= "ชื่อโดเมนเนม")
    Evidence = models.FileField(upload_to='Evidence/', null = True, blank = True)    

def __str__(self):
    return f'{self.data} : {self.OS} : {self.Rom} : {self.Ram} : {self.Services} ' 
        
