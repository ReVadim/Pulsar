from rest_framework import serializers

from src.product.models import Products


class ProductSerializer(serializers.ModelSerializer):
    """ Products serializer """

    title = serializers.CharField(required=True)
    article = serializers.CharField(required=True)

    class Meta:
        model = Products
        fields = "__all__"
