from django.contrib import admin

from .models import (
    Region,
    Supplier,
    Buyer,
    Product,
    Request
)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)
    search_fields = ('name',)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'quantity')
    list_filter = ('supplier',)
    search_fields = ('name',)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'buyer', 'quantity')
    list_filter = ('buyer',)
    search_fields = ('product_name',)
