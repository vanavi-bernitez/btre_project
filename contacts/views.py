from django.shortcuts import render, redirect
#from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # User has made an inquery?
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You've already made an inquiry for this house")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, 
        message=message, user_id=user_id)

        contact.save()

        # Send email 
        # send_mail(
        # 'Property Listing Inquiry',
        # 'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        # 'managermail@gmail.com', #email del que envio, en settins.py debe ir config este con la contraseña
        # [realtor_email, 'techguyinfo@gmail.com'], #destinatarios del correo
        # fail_silently=False
        # )

        messages.success(request, 'Request has been submitted, a realtor will contact you soon')
    
        return redirect('/listings/'+ listing_id)

