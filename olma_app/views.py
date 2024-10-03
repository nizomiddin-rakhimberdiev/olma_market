from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from olma_app.models import Product, Cart


# Create your views here.
# @login_required()
def main_page(request):
    product = Product.objects.all()
    # cart = Cart.objects.filter(user=request.user)
    # badge = len(cart)
    context = {'product': product}

    return render(request, 'index.html', context=context)


def note_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    user = request.user
    cart = Cart.objects.create(user=user, product=product)
    cart.save()
    return redirect('home')

def cart_list(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    return render(request, 'cart.html', {'cart': cart})

def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return redirect('cart-list')