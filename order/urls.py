from django.urls import path

from order.views import  confirmation, order, produit_detail
urlpatterns = [
    path('order/',  order, name="order"),
    path('confirmation/',  confirmation, name="confirmation"),
    path('produit/<int:produit_id>/', produit_detail, name='commande'),
]



