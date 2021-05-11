from django.contrib import admin

from shopping.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','original_price','discounted_price','category','description','image']





admin.site.register(Product,ProductAdmin)