from cart.templatetags.cart_tag import register


@register.simple_tag
def iterative_badge_class(number):
    while number > 3:
        number -= 3

