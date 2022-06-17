from ast import pattern
from django.urls import include,path, re_path


from . import views

app_name= 'producto_app'

urlpatterns = [
    path('api/reporte-venta/',views.ReporteVentasList.as_view(), name='reporte'),
    path('api/registrar-venta/',views.RegistrarVenta.as_view(), name='registrar'),
    path('api/registrar-venta2/',views.RegistrarVenta2.as_view(), name='registrar2'),
]