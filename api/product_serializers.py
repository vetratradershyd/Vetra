from rest_framework import serializers
from home.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "price",
            "image",
        ]


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = "__all__"