

from collections import UserList
from urllib import request
from urllib.request import Request
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from product.models import Product


class Commande(models.Model):
    
    address = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True, blank=True )
    ville = models.CharField(max_length=200, null=True, blank=True)
    pays = models.CharField(max_length=300, null=True, blank=True)
    zipcode = models.CharField(max_length=300, null=True, blank=True)
    date_livraison = models.DateField(null=True, blank=True)
    date_commande = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return str(self.date_commande)
