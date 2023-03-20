from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','password','is_active')


admin.site.register(User, UserAdmin)

