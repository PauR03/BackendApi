from . import api
from django.urls import path

# Create your views here.
urlpatterns = [
    path("api/", api.hello),
    path("api/mostrarLista/", api.mostrarLista),
    # path("api/detallesProductos/", api.detallesProductos),
    path("api/añadirProducto/", api.añadirProducto),
    # path("api/borrarProducto", api.borrarProducto),
    # path("api/editarProducto", api.editarProducto),
]