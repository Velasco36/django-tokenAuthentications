from rest_framework.generics import (
    ListAPIView,

)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .serializers import ProductSerializer
# Create your views here.
from .models import Product


class ListProductUser(ListAPIView):

    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user #recuperar el usuario
        print(usuario)


        return Product.objects.productos_por_user(usuario)


class ListProductoStok(ListAPIView):

    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user #recuperar el usuario
        print(usuario)


        return Product.objects.productos_por_user(usuario)