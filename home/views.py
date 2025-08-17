from django.shortcuts import render
from django.conf import settings
from .models import RestaurantInfo
# Create your views here.
def home(request):
    restaurant_name = getattr(settings,'RESTAURANT_NAME','Default Restaurant')
    phone="Not available"
    try:
        restaurant_info=RestaurantInfo.objects.first()
        if restaurant_info:
            phone=restaurant_info.phone
    except DatabaseError as e:
        print("Database error:",e)
        phone="Error fetching phone"
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

def reservation(request):
    restaurant_name=getattr(settings,"RESTAURANT_NAME","Default Restaurant")
    phone=RestaurantInfo.objects.first().phone if RestaurantInfo.objects.exists() else "N/A"
    return render(request,"reservation.html",{'restaurant_name':restaurant_name,'phone':phone})
