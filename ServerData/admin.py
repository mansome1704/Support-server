from django.contrib import admin
from ServerData.models import ServerData
# Register your models here.
class ServerAdmin(admin.ModelAdmin):
    list_display = ['Date','OS','Rom','Ram','Servics','DomainName']
    list_filter = ['OS','Rom','Ram','Servics']

admin.site.register(ServerData, ServerAdmin)