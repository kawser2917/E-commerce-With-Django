from django.contrib import admin
from .models import Customer,Product,Cart,OrderedPlaced

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price', 'discount_price', 'description', 'brand', 'category','product']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderedPlaced)
class OrderedPlacedAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'customer', 'product', 'quantity', 'order_date', 'status']

# Every model has a id by default
