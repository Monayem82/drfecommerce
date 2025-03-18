from rest_framework import serializers
from . models import Brand,Category,Product,ProductDetails


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"


class BradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    brand=BradSerializer()
    category= CategorySerializer()
    product_details=ProductDetailsSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        #fields="__all__"
        fields =(
            "id",
            "name",
            "description",
            "brand",
            "category",
            "product_details",
        )

