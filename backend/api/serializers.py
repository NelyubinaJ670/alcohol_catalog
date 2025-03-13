from rest_framework import serializers
from catalog.models import Supplier, Buyer, Product, Request


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'region']


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('id', 'name', 'region')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'supplier', 'quantity')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'product_name', 'organization', 'quantity')
