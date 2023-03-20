from django.contrib import admin

# Register your models here.

from django.contrib import admin
from order.models import Commande

# Register your models here.
class AdminCommande(admin.ModelAdmin):
    list_display = ('address','date_livraison','date_commande')
    search_fields = ('date_livraison', 'date_commande', 'address')
    ordering = ('address', 'date_livraison')
    filter = ('address', 'date_livraison')
    list_filter = ('address', 'date_livraison')


admin.site.register(Commande, AdminCommande)



