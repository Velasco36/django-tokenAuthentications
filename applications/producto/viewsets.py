

from rest_framework import viewsets

from .models import Colors, Product
from rest_framework.response import Response

from .serializers import (
    ColorSerializer,
    ProductSerializer,
    PaginationSerializer,
    ProductSerializerViewSet

)


class ColorViewSet(viewsets.ModelViewSet):

    serializer_class = ColorSerializer
    queryset = Colors.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer

    def perform_create(self, serializer):
        serializer.save(
            video='https://www.youtube.com/watch?v=gHgv19ip-0c&list=RDgHgv19ip-0c&start_radio=1'
        )

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.productos_por_user(self.request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)