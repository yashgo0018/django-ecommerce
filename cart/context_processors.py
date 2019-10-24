from .models import Cart


def cart_item_count(request):
    if request.user.is_authenticated:
        item_count = Cart.objects.get_existing_or_new(
            request)[0].total_cart_products()
        return {'cart_item_count': item_count}
    return {}
