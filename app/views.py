from django.core.mail import send_mail
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.list import ListView
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.contrib.auth import settings
from django.utils import timezone
from datetime import *
from django.db import models
from SosCombos_Django import settings
from SosCombos_Django.settings import CART_SESSION_ID
from app import models
from app.models import subscripciones
from cart.cart import Cart


def send_purchase_mail(lista, nombre, nombre2, email_usuario, telefono, telefono2, direccion, total):
    destinatarios = [models.general.objects.first().email]
    send_mail(
        'Nueva compra en ' + models.general.objects.first().nombre + '.\n',
        'Nueva compra, datos de compra:\nNombre de quien paga:  ' + nombre + ';\n' +
        '\nNombre de quien recibe: ' + nombre2 + ';\n' +
        '\nCorreo: ' + email_usuario + ';\n' +
        '\nTeléfono de quien paga: ' + telefono + ';\n' +
        '\nTeléfono de quien recibe: ' + telefono2 + ';\n' +
        '\nDirección: ' + direccion + ';\n' +
        '\nLista de Compra: ' + '\n' + lista + ';\n' +
        '\nPrecio total: ' + total +
        '.',
        settings.EMAIL_HOST_USER,
        destinatarios,
    )


def get_qs(self, qs):
    # FILTRAR
    if not self.request.GET.get('buscar') and not self.request.GET.get('ordenar') and not self.request.GET.get(
            'ubicacion'):
        if 'buscar' in self.request.session:
            del self.request.session['buscar']

    if self.request.GET.get('cancelar'):
        if 'ubicacion' in self.request.session:
            del self.request.session['ubicacion']

    if self.request.GET.get('clear_filter'):
        #     if 'talla' in self.request.session:
        #         del self.request.session['talla']
        #     if 'color' in self.request.session:
        #         del self.request.session['color']
        if 'category' in self.request.session:
            del self.request.session['category']
        if 'ubicacion' in self.request.session:
            del self.request.session['ubicacion']
        if 'buscar' in self.request.session:
            del self.request.session['buscar']
        if 'ordenar' in self.request.session:
            del self.request.session['ordenar']

        return qs

    if self.request.GET.get('category'):
        self.request.session['category'] = self.request.GET.get('category')
    if self.request.GET.get('ubicacion'):
        self.request.session['ubicacion'] = self.request.GET.get('ubicacion')
    if self.request.GET.get('buscar'):
        self.request.session['buscar'] = self.request.GET.get('buscar')

    if 'ubicacion' in self.request.session:
        ubi = models.ubicaciones.objects.get(ubicacion=self.request.session['ubicacion']).id
        qs = qs.filter(ubicaciones=ubi)

    if 'category' in self.request.session:
        cate = models.subCategorias.objects.get(subcategoria=self.request.session['category']).id
        qs = qs.filter(subcategoria=cate)

    if 'buscar' in self.request.session:
        bus = self.request.session['buscar']
        qs = qs.filter(nombre__icontains=bus)

    # ORDENAR
    if self.request.GET.get('ordenar'):
        self.request.session['ordenar'] = self.request.GET.get('ordenar')

    if 'ordenar' in self.request.session:
        ord = self.request.session['ordenar']
        if ord == "Menor Precio":
            qs = qs.order_by('precio')
        if ord == "Mayor Precio":
            qs = qs.order_by('-precio')
        if ord == "Más vendidos":
            qs = qs.order_by('-cantventas')

    return qs


class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data()

        context['listado_productos'] = models.productos.objects.filter(mejor=True, activ=True, especial=False)
        context['listado_productos_especiales'] = models.productos.objects.filter(especial=True, activ=True)
        context['listado_productos_completo'] = models.productos.objects.filter(activ=True)

        context['domicilio'] = models.productosDomicilio.objects.first()

        context['general'] = models.general.objects.first()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['carrusel'] = models.carrusel.objects.all()
        context['fecha'] = datetime.now()

        return context


class Productos(ListView):
    template_name = 'pages/productos.html'
    queryset = models.productos.objects.filter(activ=True).order_by('precio')
    paginate_by = 9
    context_object_name = 'productos'

    def get_queryset(self):
        qs = super(Productos, self).get_queryset()
        return get_qs(self, qs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Productos, self).get_context_data()
        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()
        context['categorias'] = models.categorias.objects.all()
        context['subcategorias'] = models.subCategorias.objects.all()
        context['cantidad'] = len(models.productos.objects.filter(activ=True))
        context['path'] = 'productos'
        context['ubicaciones'] = models.ubicaciones.objects.all()

        return context


class VerProductos(generic.DetailView):
    template_name = 'pages/verProducto.html'
    model = models.productos

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VerProductos, self).get_context_data()
        p = models.productos.objects.filter(activ=True)
        a = []
        context['listado_productos_completo'] = p
        # invertir el orden
        for x in p[::-1]:
            a.append(x)
        context['listado_ultimos_8_productos'] = a[:8]  # coger los 8 primeros de las lista invertida
        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()
        context['path'] = 'VerProductos'

        return context


class SobreNosotros(generic.TemplateView):
    template_name = 'pages/sobreNosotros.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SobreNosotros, self).get_context_data()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


class CondicionesUso(generic.TemplateView):
    template_name = 'pages/condicionesUso.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CondicionesUso, self).get_context_data()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


class EnviosDevoluciones(generic.TemplateView):
    template_name = 'pages/enviosDevoluciones.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EnviosDevoluciones, self).get_context_data()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


class PoliticaPrivacidad(generic.TemplateView):
    template_name = 'pages/politicaPrivacidad.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PoliticaPrivacidad, self).get_context_data()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


class Contacto(generic.TemplateView):
    template_name = 'pages/contacto.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Contacto, self).get_context_data()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


class Carrito(generic.TemplateView):
    template_name = 'pages/carrito.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Carrito, self).get_context_data()
        context['path'] = 'carrito'
        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


@require_POST
def Subscribe(request):
    subs = models.subscripciones(email=request.POST["email"])
    subs.save()
    return redirect('index')


class Pago(generic.TemplateView):
    template_name = 'pages/pago.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Pago, self).get_context_data()

        context['conocenos'] = models.conocenos.objects.first()
        context['contactenos'] = models.contactenos.objects.first()
        context['general'] = models.general.objects.first()

        return context


# VIEWS DE CART
# Adding an element
@method_decorator(csrf_exempt, require_POST)
def add(request: HttpRequest):
    cart = Cart(request)
    id = request.POST['id']
    cart.add(product=models.productos.objects.filter(id=id).first())
    return JsonResponse({"result": "ok",
                         "amount": cart.session[CART_SESSION_ID].get(id, {"quantity": 0})["quantity"]
                         })


# cambiando el carrito para aceptar varios elementos
@method_decorator(csrf_exempt, require_POST)
def add_n_productos(request: HttpRequest):
    cart = Cart(request)
    id = request.POST['id']
    quantity = request.POST['quantity']
    cart.add(product=models.productos.objects.filter(id=id).first(), quantity=quantity)
    return JsonResponse({"result": "ok",
                         "amount": cart.session[CART_SESSION_ID].get(id, {"quantity": 0})["quantity"]
                         })


# Cleaning the cart
@require_POST
def cart_clear(request: HttpRequest):
    Cart(request).clear()
    return redirect('carrito')


# Remove all elements of a type from cart
@method_decorator(csrf_exempt, require_POST)
def item_clear(request: HttpRequest):
    cart = Cart(request)
    id = request.POST['id']
    cart.remove(product=models.productos.objects.filter(id=id).first())
    return JsonResponse({
        "result": "ok",
        "amount": cart.get_sum_of("quantity")
    })


# Remove element
@method_decorator(csrf_exempt, require_POST)
def remove(request: HttpRequest):
    id = request.POST['id']
    Cart(request).decrement(product=models.productos.objects.filter(id=id).first())
    return JsonResponse({"result": "ok"})


# Adding N elements to cart
@require_POST
def add_quant(request: HttpRequest, id: int, quantity: int):
    cart = Cart(request)
    cart.add(models.productos.objects.filter(id=id).first(), quantity)
    return JsonResponse({"result": "ok",
                         "amount": cart.session[CART_SESSION_ID].get(id, {"quantity": quantity})["quantity"]})


# aumentando la cantidad de ventas de un producto
@method_decorator(csrf_exempt, require_POST)
def aumentar_ventas(request: HttpRequest, id: int, quantity: int):
    actual_quantity = int(models.productos.objects.get(id=id).cantventas)
    models.productos.objects.filter(id=id).update(cantventas=actual_quantity + int(quantity))
    return JsonResponse({"result": "ok",
                         "amount": models.productos.objects.get(id=id).cantventas
                         })


# añadiendo elementos a tabla venta
@method_decorator(csrf_exempt, require_POST)
def registar_venta(request: HttpRequest):
    lista = request.POST['lista']
    total_price = request.POST['total_price']
    name = request.POST['name']
    name2 = request.POST['name2']
    email = request.POST['email']
    phone = request.POST['phone']
    phone2 = request.POST['phone2']
    provincia = request.POST['country']
    municipio = request.POST['city']
    address = request.POST['address']

    newventa = models.venta(lista=lista, precio_total=total_price, nombre=name, nombre2=name2, email=email,
                            direccion=address, ciudad=municipio,
                            pais=provincia, telefono=phone, telefono2=phone2)
    newventa.save()

    return JsonResponse({"result": "ok",
                         })


# nuevo correo de compra
@method_decorator(csrf_exempt, require_POST)
def new_purchase_mail(request: HttpRequest):
    lista = request.POST['lista']
    nombre = request.POST['name']
    nombre2 = request.POST['name2']
    email_remitente = request.POST['email']
    telefono = request.POST['phone']
    telefono2 = request.POST['phone2']
    direccion = request.POST['address']
    total = request.POST['total']
    send_purchase_mail(lista, nombre, nombre2, email_remitente, telefono, telefono2, direccion, total)
