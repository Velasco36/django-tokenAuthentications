from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()

router.register(r'ventas', viewsets.VentaViewsets, basename="ventas")

urlpatterns = router.urls