from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from myapp.models import Product
from django.http import JsonResponse

# Cart Summary View
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()  # Corrected method call
    return render(request, 'cart_summary.html', {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals  # Pass the total to the template
    })


# Add Product to Cart View
def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)

        # Adding product to cart
        cart.add(product=product,quantity=product_qty)
        cart_quantity = cart.__len__()
        # Return response with product name
        response = JsonResponse({'qty': cart_quantity})
        return response

# Delete Product from Cart View
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response

# Update Product Quantity in Cart View
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quntity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
        return redirect('cart_summary')