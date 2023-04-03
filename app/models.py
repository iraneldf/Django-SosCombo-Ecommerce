from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.forms import model_to_dict
from solo.models import SingletonModel

# Create your models here.
from SosCombos_Django import settings


class general(SingletonModel):
    nombre = models.CharField(max_length=14, verbose_name='Nombre de la empresa', default='', unique=True)
    entrega = models.CharField(max_length=50, verbose_name='Tiemp de entrega', default='', unique=True)
    logo = models.ImageField(verbose_name='Logo', upload_to='img/logo/', null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio de envio', default=0)
    id_paypal = models.CharField(max_length=100, verbose_name='Id de Paypal', default='', null=True, blank=True,
                                 unique=True)

    class Meta:
        verbose_name = '00- General'


class carrusel(models.Model):
    imagen = models.ImageField(verbose_name='Imagen', upload_to='img/carrusel/', null=True, blank=True)
    texto = models.CharField(verbose_name='Texto', default='', max_length=100)

    class Meta:
        verbose_name_plural = '01- Carrusel'
        verbose_name = 'Elemento de carrusel'

    def __str__(self):
        return self.texto


class categorias(models.Model):
    categoria = models.CharField(max_length=100, verbose_name='Categoría', default='')

    class Meta:
        verbose_name_plural = '08- Categorias'

    def __str__(self):
        return self.categoria


class ubicaciones(models.Model):
    ubicacion = models.CharField(max_length=100, verbose_name='ubicacion')

    def __str__(self):
        return self.ubicacion


class subCategorias(models.Model):
    categoria = models.ForeignKey(categorias, verbose_name='Categoría', on_delete=models.CASCADE, unique=True)
    subcategoria = models.CharField(max_length=100, verbose_name='Subcategoría', default='')

    class Meta:
        verbose_name_plural = '09-Subcategorias'

    def __str__(self):
        # return self.subcategoria + "(" + self.categorias + ")"
        return f"{self.subcategoria} ({self.categoria})"


class productos(models.Model):
    activ = models.BooleanField(default=True, verbose_name='Mostrar')
    imagen = models.ImageField(verbose_name='Imagen', upload_to='img/productos/')
    nombre = models.CharField(max_length=100, verbose_name='Nombre', default='')
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')
    mejor = models.BooleanField(default=True, verbose_name='Marcar como uno de los mejores productos')
    especial = models.BooleanField(default=True, verbose_name='Oferta especial')
    subcategoria = models.ManyToManyField(subCategorias)
    ubicaciones = models.ManyToManyField(ubicaciones)
    cantventas = models.PositiveIntegerField(verbose_name='Cantidad de ventas', editable=False, auto_created=True,
                                             default=0)

    class Meta:
        verbose_name_plural = '02- Productos'
        verbose_name = 'Producto'

    def __str__(self):
        if self.activ:
            result = "Mostrado"
        else:
            result = "Sin mostrar"
        return self.nombre + ' (' + result + ')'

    def toJSON(self):
        item = model_to_dict(self)
        del item['subcategoria']
        del item['activ']
        del item['mejor']
        del item['especial']
        del item['ubicaciones']
        item['imagen'] = self.imagen.url
        item['precio'] = float(self.precio)

        return item

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # if self.activ:
        #     destinatarios = []
        #     for dest in subscripciones.objects.all():
        #         destinatarios.append(dest.email)
        #
        #     url = Site.objects.get_current().domain
        #
        #     send_mail(
        #         "SosCombo",
        #         "Hola! Tenemos nuevos productos visítanos en: " + url,
        #         settings.EMAIL_HOST_USER,
        #         destinatarios,
        #     )

        return super(productos, self).save()


class productosDomicilio(SingletonModel):
    imagen = models.ImageField(default='img/banner 2.jpg', verbose_name='Imagen', upload_to='img/Productos Domicilio/')
    encabezado = models.CharField(max_length=100, verbose_name='Encabezado')
    texto = models.CharField(max_length=1000, verbose_name='Texto')

    class Meta:
        verbose_name = '03- Pedidos a domicilio'


class conocenos(SingletonModel):
    sobreNosotros = models.CharField(max_length=100, verbose_name='Sobre nosotros', default='Sobre nosotros')
    condiciones = models.CharField(max_length=100, verbose_name='Condiciones de uso', default='Condiciones de uso')
    envio = models.CharField(max_length=100, verbose_name='Envíos y Devoluciones', default='Envíos y Devoluciones')
    politica = models.CharField(max_length=100, verbose_name='Política de Privacidad', default='Política de Privacidad')

    class Meta:
        verbose_name = '04- Conócenos'


class contactenos(SingletonModel):
    telef = models.CharField(max_length=100, verbose_name='Teléfono', default='')
    email = models.EmailField(max_length=100, verbose_name='Correo', default='soscombos@gmail.com')
    email_en = models.URLField(max_length=1000, verbose_name='Enlace de correo')

    class Meta:
        verbose_name = '05- Contáctenos'


class subscripciones(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Correo')

    class Meta:
        verbose_name_plural = '06- Subscripciones'
        verbose_name = 'subscripción'

    def __str__(self):
        return self.email


class venta(models.Model):
    # campos
    producto = models.CharField(max_length=100, verbose_name='Nombre del producto')
    precio = models.FloatField(verbose_name='Precio')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad de unidades del producto')
    precio_total = models.FloatField(verbose_name='Precio total')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del cliente')
    email = models.EmailField(verbose_name='Correo del cliente')
    direccion = models.CharField(verbose_name='Direccion', max_length=200)
    ciudad = models.CharField(verbose_name='Cudad', max_length=100)
    pais = models.CharField(verbose_name='País', max_length=100)
    telefono = models.CharField(verbose_name='Phone', max_length=30)

    class Meta:
        verbose_name_plural = 'Ventas'
        verbose_name = 'Venta'

    def __str__(self):
        return f"{self.nombre} | {self.email} | {self.producto} X {self.cantidad} | ${self.precio_total} " \
               f"| {self.ciudad} | {self.pais} | {self.telefono} "
