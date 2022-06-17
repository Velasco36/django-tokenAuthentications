from django.db import models


class SaleDatailManager(models.Manager):

    def productos_por_venta(self, venta_id):
        consulta = self.filter(
            sale_id=venta_id
        ).order_by('count', 'product_name')
        return consulta