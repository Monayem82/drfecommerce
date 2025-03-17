from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .import views

router=DefaultRouter()
router.register(r'category',views.CategoroyViewSet,basename='categories')
router.register(r'brand',views.BrandViewSet,basename='brands')
router.register(r'product',views.ProductViewSet,basename='product')

urlpatterns=[
    path('api/',include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]