from django.contrib import admin
from .models import *

class Dishes_admin(admin.ModelAdmin):
    list_display = ['id', 'dishes_name', 'description', 'photo', 'category_id']
    list_display_links = ['id', 'dishes_name']

class Dishes_category_admin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['id', 'type']

class Contact_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact']
    list_display_links = ['id', 'name', 'contact']

admin.site.register(Dishes_Category, Dishes_category_admin)
admin.site.register(Dishes, Dishes_admin)
admin.site.register(Contact, Contact_Admin)