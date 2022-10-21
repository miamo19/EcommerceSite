from django.contrib import admin
from store.models import Product

# Register your models here.
admin.site.site_title = "shop"
admin.site.site_header = "E-Commerce"
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'date_added')
admin.site.register(Product, AdminProduct)
