from ast import pattern
from django.urls import include,path, re_path


from . import views

app_name= 'producto_app'

urlpatterns = [
    path('api/product/por-users/',views.ListProductUser.as_view(), name='producto-users'),
]