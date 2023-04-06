from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('productos', Productos.as_view(), name='productos'),
    path('VerProducto/<int:pk>', VerProductos.as_view(), name='VerProductos'),
    path('sobreNosotros', SobreNosotros.as_view(), name='sobreNosotros'),
    path('condicionesUso', CondicionesUso.as_view(), name='condicionesUso'),
    path('enviosDevoluciones', EnviosDevoluciones.as_view(), name='enviosDevoluciones'),
    path('politicaPrivacidad', PoliticaPrivacidad.as_view(), name='politicaPrivacidad'),
    path('contacto', Contacto.as_view(), name='contacto'),
    path('carrito', Carrito.as_view(), name='carrito'),
    path('subscribe', Subscribe, name='subscribe'),
    path('pago', Pago.as_view(), name='pago'),

    # custom
    path("sales/add/<id>/<quantity>", aumentar_ventas, name="aumentar_venta"),
    path("venta/add", registar_venta, name="registar_venta"),
    path("venta/mail", new_purchase_mail, name="venta_mail")

]
# urls de cart
urlpatterns += [
    path("cart/add/", add, name="cart_add"),
    path("cart/remove/", remove, name="cart_remove"),
    path("cart/clear/", cart_clear, name="cart_clear"),
    path("cart/clear/id", item_clear, name="cart_clear_id"),
    path("cart/cartAjax/", add_n_productos, name="cartAjax"),
    # path("cart/details/<id>/", cart_detail, name="cart_details"),
]
