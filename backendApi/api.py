from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view
# from rest_framework.decorators import api_view

def hello(request):
    # jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

def mostrarLista(request):
    productos = Producto.objects.values('id', 'nombre')
    return JsonResponse({
        "data": list(productos)
    })

@api_view(['POST'])
def detallesProductos(request):
    print(request.data)
    producto = Producto.objects.filter(id=request.data.get('id_producto')).values('nombre', 'descripcion', 'precio')
    if producto:
        return JsonResponse({
        "data": list(producto)
    })
    else:
        return JsonResponse({
            "status": "Error",
            "message": "Producto not found"
        })

@api_view(['POST'])
def añadirProducto(request):
    try:
        producto = Producto.objects.create(
            nombre = request.data.get('nombre'),
            descripcion = request.data.get('descripcion'),
            precio = request.data.get('precio')
        )
        return JsonResponse({
            "status": True
        })
    except:
        return JsonResponse({
            "status": False
        })

@api_view(['POST'])
def borrarProducto(request):
    try:
        producto = Producto.objects.get(id=request.data.get('id'))
        producto.delete()
        return JsonResponse({
            "status": True
        })
    except:
        return JsonResponse({
            "status": False
        })
    
@api_view(['POST'])
def editarProducto(request):
    try:
        producto = Producto.objects.get(id=request.data.get('id'))
        producto.nombre = request.data.get('nombre')
        producto.descripcion = request.data.get('descripcion')
        producto.precio = request.data.get('precio')
        producto.save()
        return JsonResponse({
            "status": True
        })
    except:
        return JsonResponse({
            "status": False
        })