from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .import views

router=DefaultRouter()
router.register(r'category',views.CategoroyViewSet,basename='categories')
router.register(r'brand',views.BrandViewSet,basename='brands')
router.register(r'product',views.ProductViewSet,basename='product')

urlpatterns=[
    path('api/',include(router.urls)),
]