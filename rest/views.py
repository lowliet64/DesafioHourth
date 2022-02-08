from .models import Product
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-product_url_created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]