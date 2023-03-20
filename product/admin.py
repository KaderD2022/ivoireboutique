from django.contrib import admin
from product.models import Product


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'slug','description','company','image','price','type','etat','stock','number_register')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('company', 'etat', 'type')
    ordering = ('type', 'number_register')
    filter = ('number_register', 'company')
    list_filter = ('number_register', 'company')


admin.site.register(Product, AdminProduct)