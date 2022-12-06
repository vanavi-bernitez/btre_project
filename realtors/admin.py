from django.contrib import admin

from .models import Realtor   #from models file inside realtors folder, import the class called REaltor (the model, in other words)

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name',)
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)  #vamo a registrar el modelo Realtor para que aparezca en el lado del admin en la pagina 


