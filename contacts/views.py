from django.shortcuts import render, redirect
from django.contrib import messages
from operator import itemgetter
from django.core.mail import send_mail

from .models import Contact

def contact(request):
  if request.method == "POST":
    listing_id, listing, name, email, phone, message, user_id, realtor_email = itemgetter('listing_id', 'listing', 'name', 'email', 'phone', 'message', 'user_id', 'realtor_email')(request.POST)

    # Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'Inquiry already sent')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
    contact.save()

    # Send email
    send_mail(
      # Subject
      'Property Listing Inquiry',
      # Body
      'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
      # Sender smtp server
      'kristian.y100@gmail.com',
      # Recipients CC
      [realtor_email, 'dcnan@live.com'],
      fail_silently = False
    )

    messages.success(request, 'Thank you, your enquiry has been sent.')
    return redirect('/listings/'+listing_id)