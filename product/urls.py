from django.urls import path, include
from product.views import index, detail


urlpatterns = [
    path('', index, name="home"),
    path('detail/<slug>/', detail, name="detail"),
]
