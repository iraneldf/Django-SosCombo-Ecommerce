from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from app import models


class ProductoAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre', 'precio', 'activ', 'mejor', 'especial')


class GeneralAdmin(SingletonModelAdmin):
    fieldsets = [
        ('Configuraciones Básicas', {
            'fields': ('nombre', 'logo')
        },),
        ('Configuraciones Avanzadas', {
            'fields': ('email', 'precio', 'entrega', 'id_paypal')
        },),

    ]


class VentasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre2', 'email', 'precio_total')


admin.site.register(models.general, GeneralAdmin)
admin.site.register(models.carrusel)
admin.site.register(models.productos, ProductoAdmin)
admin.site.register(models.productosDomicilio, SingletonModelAdmin)
admin.site.register(models.conocenos, SingletonModelAdmin)
admin.site.register(models.contactenos, SingletonModelAdmin)
admin.site.register(models.subscripciones)
admin.site.register(models.categorias)
admin.site.register(models.subCategorias)
admin.site.register(models.ubicaciones)
admin.site.register(models.venta, VentasAdmin)
