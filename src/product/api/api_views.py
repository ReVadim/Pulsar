from rest_framework.viewsets import ModelViewSet

from src.product.models import Products
from .serializers import (
    ProductSerializer,
)


class ProductViewSet(ModelViewSet):
    """ Products ViewSet """

    throttle_scope = 'anon'
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

