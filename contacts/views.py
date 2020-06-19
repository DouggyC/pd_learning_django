from django.shortcuts import render, redirect
from django.contrib import messages
from operator import itemgetter

from .models import Contact

# Create your views here.
def contact(request):
  if request.method == "POST":
    listing_id, listing, name, email, phone, message, user_id, realtor_email = itemgetter('listing_id', 'listing', 'name', 'email', 'phone', 'message', 'user_id', 'realtor_email')(request.POST)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
    contact.save()

    messages.success(request, 'Thank you, your enquiry has been sent.')
    return redirect('/listings/'+listing_id)