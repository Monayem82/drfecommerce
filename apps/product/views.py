from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from apps.product.serializers import ProductSerializer,CategorySerializer,BradSerializer

from . models import Brand,Category,Product



class CategoroyViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BradSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
