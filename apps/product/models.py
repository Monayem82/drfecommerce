from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Brand(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name=models.CharField(max_length=50)
    parent=TreeForeignKey('self',on_delete=models.PROTECT,null=True,blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    is_digital=models.BooleanField(default=False)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=TreeForeignKey('Category',on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    price=models.DecimalField(decimal_places=3,max_digits=10)
    stock_qty=models.IntegerField()
    sku=models.CharField(max_length=100)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_details")
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.price} - {self.sku}"