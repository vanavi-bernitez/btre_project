from django.shortcuts import get_object_or_404, render
from .models import Listing # llamar el archivo .models.py from the self folder
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import *

def index(request):
    listings = Listing.objects.all().order_by('id').filter(is_published = True) #this fetch all of the listings that fits the filter parameter
    paginator = Paginator(listings, per_page=3)
    page = request.GET.get('page') #page is an URL parameter https://realpython.com/django-pagination/
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings  #pass it as a dictionary 
    }
    return render(request, 'listings/listings.html', context) #the second value is a dic, where im gonna display the inf to the fron

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk= listing_id)
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #search for filtering 
    #keywords
    if 'keywords' in request.GET:  #check if exist, using the get request test
        keywords = request.GET['keywords']  #get that value from input field keywords 
        if keywords:  #its not empty
            queryset_list = queryset_list.filter(description__icontains = keywords)  #not exactly word match. Review if X paragraph contains the word

    #city
    if 'city' in request.GET:  #check if exist, using the get request test
        city = request.GET['city']  #get that value from input field keywords 
        if city:  #its not empty
            queryset_list = queryset_list.filter(city__iexact = city) #exact match

    #state
    if 'state' in request.GET:  
        state = request.GET['state']  
        if state:  
            queryset_list = queryset_list.filter(state__icontains = state)

    #bedrooms
    if 'bedrooms' in request.GET:  
        bedrooms = request.GET['bedrooms']  
        if bedrooms:  
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms) #you know what it means :)

    #price
    if 'price' in request.GET:  
        price = request.GET['price']  
        if price:  
            queryset_list = queryset_list.filter(price__lte = price)


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)