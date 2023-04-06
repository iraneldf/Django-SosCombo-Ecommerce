from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from app import models

admin.site.register(models.general, SingletonModelAdmin)
admin.site.register(models.carrusel)
admin.site.register(models.productos)
admin.site.register(models.productosDomicilio, SingletonModelAdmin)
admin.site.register(models.conocenos, SingletonModelAdmin)
admin.site.register(models.contactenos, SingletonModelAdmin)
admin.site.register(models.subscripciones)
admin.site.register(models.categorias)
admin.site.register(models.subCategorias)
admin.site.register(models.ubicaciones)
admin.site.register(models.venta)

