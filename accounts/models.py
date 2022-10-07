from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length= 20, null = True, blank = True)
    age = models.PositiveIntegerField(null = True, blank = True)