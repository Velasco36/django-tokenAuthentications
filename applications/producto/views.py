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
    # verifica que el token pertenezca a un usuario
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #recuperar el usuario
       #usuario = self.request.user 
        #print(usuario)
        return Product.objects.productos_con_stok()


class ListProductoGenero(ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        #recuperaar para clave o parametro     
        genero = self.kwargs['gender']
        return Product.objects.productos_por_genero('genero')


class FilterProductos(ListAPIView):  #video 158 error

    serializer_class = ProductSerializer

    def get_queryset(self):
        varon = self.request.query_params.get('man', None)
        mujer = self.request.query_params.get('woman', None)
        nombre = self.request.query_params.get('name', None)
        #

        return  Product.objects.filtrar_productos(
            man=self.request.query_params.get('man', None),
            woman = self.request.query_params.get('woman', None),
            name = self.request.query_params.get('name', None)
        )

        