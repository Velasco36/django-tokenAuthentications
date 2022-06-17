from dataclasses import field
from rest_framework import serializers

from .models import Sale, SaleDetail



class VentaReporteSerializers(serializers.ModelSerializer):



    class Meta:
        model = Sale
        fields = (
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',
        )

    
    def get_productos(self,obj):
        query = SaleDetail.objects.productos_por_venta(obj.id)
        productos_realizados = DetalleVentaProductosSerializer(query, many=True).data

        return productos_realizados

class DetalleVentaProductosSerializer(serializers.ModelSerializer):
    class Meta:
         model =SaleDetail
         fields =(
             'id',
             'sale',
             'product',
             'count',
             'price_purchase',
             'price_sale'
         )



class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()

class ProductoDetailSerializers(serializers.Serializer):
    
    pk = serializers.IntegerField()
    count = serializers.IntegerField()

class ProcesoVentaSerializer(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ProductoDetailSerializers(many=True)

class ProcesoVentaSerializer2(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ArrayIntegerSerializer()
    cantidades = ArrayIntegerSerializer()

    def validate(self, data):
        if data['type_payment'] != '0':
            raise serializers.ValidationError('ingrese un tipo de pago correcto')

        return data
    
    def validate_type_invoce(self, value):
        if value != '0':
            raise serializers.ValidationError('ingrese un valor correcto')

        return value
