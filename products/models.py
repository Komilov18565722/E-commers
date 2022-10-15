from itertools import product
from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Product (models.Model):
    title = models.CharField(max_length=30)
    bio = models.CharField(max_length=50)
    definition = models.TextField()
    photo1 = models.ImageField(upload_to = 'media/img/product-img/%Y/%m/%d')
    photo2 = models.ImageField(upload_to = 'media/img/product-img/%Y/%m/%d', null = True, blank = True)
    photo3 = models.ImageField(upload_to = 'media/img/product-img/%Y/%m/%d', null = True, blank = True)
    photo4 = models.ImageField(upload_to = 'media/img/product-img/%Y/%m/%d', null = True, blank = True)
    price = models.FloatField(default = 0.00)
    count = models.PositiveIntegerField(default = 1)
    delivery_price = models.FloatField(default = 0.00)
    users = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True, blank = True)
    card = models.BooleanField(default = 0)
    buy =  models.BooleanField(default = 0)
    
    def __str__(self):
        return self.title

