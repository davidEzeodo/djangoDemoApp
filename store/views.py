from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Serializers import serializers, ProductSerializer
from .models import Product


# Create your views here.

@api_view()
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


