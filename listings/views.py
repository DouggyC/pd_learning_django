from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'listings/listings.html')

def listing(request, listing_id):
  return render(request, 'listing/listing.html')

def search(request):
  return render(request, 'listing/search.html')