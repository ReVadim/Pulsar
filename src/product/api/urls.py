from django.urls import path
from rest_framework.routers import DefaultRouter

from src.product.api.api_views import (
    ProductViewSet,
)


router = DefaultRouter()

router.register('product', ProductViewSet, basename='product')


urlpatterns = [

]
