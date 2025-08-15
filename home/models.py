from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    phone = models.CharField(max_length=15)