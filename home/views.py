from django.shortcuts import render
from django.conf import settings
from .models import RestaurantInfo
# Create your views here.
def home(request):
    restaurant_name = getattr(settings,'RESTAURANT_NAME','Default Restaurant')
    restaurant_info=RestaurantInfo.objects.first()
    phone=restaurant_info.phone if restaurant_info else "N/A"
    return render('home.html',{'restaurant_name':restaurant_name,'phone':phone})


def about(request):
    restaurant_name=Restaurant.objects.first().name
    return render(request,'about.html',{'restaurant_name':restaurant_name})

def custom_404_view(request,exception=None):
    #try to fetch resturant name(fallback to setting)
    if resturant.objects.exists():
        restaurant_name=Restaurant.objects.first().name
    else:
        restaurant_name=getattr(settings,"RESTAURANT_NAME",'Our Restaurant')
    return render(request,"404.html",{"restaurant_name":restaurant_name})

