from django.contrib import admin

from .models import Listing   #from models file inside listings folder, import the class called Listing (the model, in other words)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title',) #when i lock the cursor over this specific fields, i can open the item
    list_filter =  ('realtor',) #create a filter box with the param i specified. IMPORTANT: <,> at the end to avoid error, bcs this must be a tuple or a list 
    list_editable = ('is_published', ) # enable the editable for the feature i specified
    search_fields = ('title', 'price') #create a search bar and filter with the specified fields
    list_per_page = 25 #define the amount of items per pages

admin.site.register(Listing, ListingAdmin)  #vamo a registrar el modelo Listing para que aparezca en el lado del admin en la pagina 
