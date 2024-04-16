from django.core.management.base import BaseCommand
from faker import Faker
from backendApi.models import Producto  # Corregido el nombre del modelo

fake = Faker()

class Command(BaseCommand):
    help = 'Crea productos'

    def handle(self, *args, **kwargs):
        for _ in range(10):
            producto = Producto.objects.create(
                nombre=fake.company(),
                descripcion=fake.text(),
                precio=fake.pydecimal(left_digits=3, right_digits=2, positive=True)  # Generar un decimal aleatorio
            )
            
        self.stdout.write(self.style.SUCCESS('Productos creados'))
