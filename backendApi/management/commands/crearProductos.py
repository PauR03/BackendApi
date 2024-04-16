from django.core.management.base import BaseCommand
from backendApi.models import Producto
from faker import Faker

fake = Faker(["es_ES"])

class Command(BaseCommand): 
    help = 'Crea productos'

    def handle(self, *args, **kwargs):
        for i in range(10):
            producto = Producto.objects.create(
                nombre=fake.word(),
                descripcion=fake.text(),
                precio=fake.pydecimal(left_digits=3, right_digits=2, positive=True)  # Generar un decimal aleatorio
            )
            
        self.stdout.write(self.style.SUCCESS('Productos creados'))
