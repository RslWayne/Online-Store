import contacts as contacts
from django.contrib import admin
from .models import*
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = 'name','image','descrption'
admin.site.register([Product],)
admin.site.register([Order,AboutUs,Contacts,Profile])
