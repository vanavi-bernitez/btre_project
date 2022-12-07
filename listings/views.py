from django.shortcuts import render
from .models import Listing # llamar el archivo .models.py 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    listings = Listing.objects.all().order_by('id') #this fetch all of the listings
    paginator = Paginator(listings, per_page=3)
    page = request.GET.get('page') #page is an URL parameter https://realpython.com/django-pagination/
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings  #pass it as a dictionary 
    }
    return render(request, 'listings/listings.html', context) #the second value is a dic, where im gonna display the inf to the fron

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')