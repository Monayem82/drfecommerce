from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from apps.product.serializers import ProductSerializer,CategorySerializer,BradSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


from . models import Brand,Category,Product



class CategoroyViewSet(viewsets.ViewSet):
    serializer_class =CategorySerializer

    @extend_schema(request=CategorySerializer)
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    serializer_class =BradSerializer

    @extend_schema(request=BradSerializer)
    def list(self, request):
        return super().list(request)


class ProductViewSet(viewsets.ViewSet):
    serializer_class =ProductSerializer
    @extend_schema(request=ProductSerializer)
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
