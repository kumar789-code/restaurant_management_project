from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)

class Feedback(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    comments=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    