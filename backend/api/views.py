from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from catalog.models import Supplier, Buyer, Product, Request

from .serializers import SupplierSerializer, BuyerSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['post'])
    def find_buyers(self, request, pk=None):
        supplier = self.get_object()
        results = self.find_buyers_for_supplier(supplier)
        return Response(results, status=status.HTTP_200_OK)

    def find_buyers_for_supplier(self, supplier):
        results = []
        for product in supplier.products.all():
            requests = Request.objects.filter(product_name=product.name, organization__region=supplier.region)
            for request in requests:
                results.append(f'Организация {request.organization.name} ({request.organization.region}) ищет продукт {request.product_name}')
        return results


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

    @action(detail=True, methods=['post'])
    def find_suppliers(self, request, pk=None):
        organization = self.get_object()
        results = self.find_suppliers_for_organization(organization)
        return Response(results, status=status.HTTP_200_OK)

    def find_suppliers_for_organization(self, organization):
        results = []
        for request in organization.requests.all():
            products = Product.objects.filter(name=request.product_name, supplier__region=organization.region)
            for product in products:
                results.append(f'Поставщик {product.supplier.name} ({product.supplier.region}) продает продукт {product.name}')
        return results
