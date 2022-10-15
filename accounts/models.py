from django.db import models
from django.contrib.auth.models import AbstractUser

# from products.models import Product
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length= 20, null = True, blank = True)
    age = models.PositiveIntegerField(null = True, blank = True)
    # cards = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, blank = True)
