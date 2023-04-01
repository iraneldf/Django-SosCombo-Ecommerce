from django.test import TestCase

# Create your tests here.
from app.models import productos

print(productos.objects.filter(categoria__categoria='de agro'))
