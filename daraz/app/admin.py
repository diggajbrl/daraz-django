from django.contrib import admin
from . models import Mens, Womens, Product

class MensAdmin (admin.ModelAdmin) :
    search_fields = ('description',)
    list_display = ('image', 'description', 'price')
admin.site.register(Mens, MensAdmin)

class WomenAdmin (admin.ModelAdmin) :
    search_fields = ('description',)
    list_filter = ('categories',)
    list_display = ('image', 'img_alt', 'categories', 'description', 'currency', 'price')
admin.site.register(Womens, WomenAdmin)

class ProductAdmin (admin.ModelAdmin) :
    search_fields = ('description',)
    list_filter = ('categories',)
    list_display = ('image', 'img_alt', 'categories', 'description', 'size', 'currency', 'price')
admin.site.register(Product, ProductAdmin)