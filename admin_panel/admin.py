from django.contrib import admin
from .models import Shop, Manufacturer, Category


# Register your models here.
admin.site.register(Shop)
admin.site.register(Manufacturer)
admin.site.register(Category)
