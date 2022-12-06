from django.db import models
from datetime import datetime
from realtors.models import Realtor #from folder realtors, file models.py import model Reaaltor

# I define a model using a class

class Listing(models.Model):
    # ForeignKey(0,1)   
    # [0] where the key comes from
    # [1] what to do if it's deleted in the origin model. 
    # In this case, the listings keeps even if the realtor got deleted 
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 20)
    description = models.TextField(blank = True) #blank means this field is optional
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits = 2, decimal_places = 1) #digits in total, and total of decimals
    garage = models.IntegerField(default = 0)
    sqft = models.IntegerField
    lot_size = models.DecimalField(max_digits = 5, decimal_places= 1)
    photo_main = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
    photo_2 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
    photo_6 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)

    #what i'm gonna display in the admin area. This is the inf i show. otherwise, shows the id
    def __str__(self):
        return self.title  
