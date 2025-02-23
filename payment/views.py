# views.py
from django.shortcuts import render
from cart.cart import Cart
from payment.models import ShippingAddress
from payment.forms import ShippingForm

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()  
    return render(request, 'payment/checkout.html', {
    "cart_products": cart_products,
    "quantities": quantities,
    "totals": totals  
})



def payment_success(request):
    return render(request, "payment/payment_success.html",{})

def billing(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
     
    if request.user.is_authenticated :
        return render(request, 'payment/billing.html', {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_info": request.POST
        })


