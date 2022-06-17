from ast import pattern
from django.urls import include,path, re_path


from . import views

app_name= 'producto_app'

urlpatterns = [
    path('api/product/por-users/',views.ListProductUser.as_view(), name='producto-users'),
    path('api/product/con-stok/',views.ListProductoStok.as_view(), name='producto-stok'),
    path('api/product/genero/<gender>/',views.ListProductoGenero.as_view(), name='producto-genero'),
    path('api/product/filter/',views.FilterProductos.as_view(), name='producto-filtrar'),
]

