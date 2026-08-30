from rest_framework import viewsets
from home.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .product_serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
)

from rest_framework import generics


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class ProductViewSet(generics.ListCreateAPIView):
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):

        if self.action == "list":

            return ProductListSerializer

        return ProductDetailSerializer


    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "category",
        "is_available",
        "is_featured",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "price",
        "created_at",
        "name",
    ]

    ordering = ["name"]