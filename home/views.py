from django.shortcuts import render
from django.conf import settings
# Create your views here.
def home(request):
    restaurant_name = getattr(settings,'RESTAURANT_NAME','Default Restaurant')
    return render('home.html',{'restaurant_name':restaurant_name})
