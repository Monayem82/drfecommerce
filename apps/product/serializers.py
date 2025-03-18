from rest_framework import serializers
from . models import Brand,Category,Product,ProductDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

