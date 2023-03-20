from django.db import models

# Create your models here.
class Product(models.Model):
    TYPE_CHOICES = (
        ('b6', 'B6'), 
        ('b12', 'B12'),
    )
    ETAT_CHOICES = (
        ('nouvelle', 'Nouvelle'),
        ('ncien', 'Ancien'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(max_length=255)
    company = models.CharField(max_length=255)
    image = models.CharField(max_length=1000000000)
    price = models.IntegerField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default="b6")
    etat = models.CharField(choices=ETAT_CHOICES, max_length=20, default="ancien")
    stock = models.IntegerField()
    number_register = models.CharField(max_length=255)

        
    def __str__(self):
        return self.title
