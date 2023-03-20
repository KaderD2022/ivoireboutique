from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255,null=True, blank=True)
    sexe = models.CharField(max_length=15,null=True, blank=True)




