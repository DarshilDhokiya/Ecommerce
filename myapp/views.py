from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product  # Use the corrected model name 'Product'
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm
from django import forms
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from cart.cart import Cart

 
def search(request):
    query = request.GET.get('query', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'myapp/search_results.html', {'query': query, 'results': results})

def shipping_info(request):
    if request.user.is_authenticated:
        # Retrieve or create a shipping address for the current user
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        
        if request.method == 'POST' and shipping_form.is_valid():
            # Save the form data
            shipping_form.save()
            messages.success(request, "Shipping information saved successfully.")
            # Redirect to the billing page
            return redirect('billing')  # Redirect to the billing page

        return render(request, 'myapp/shipping_info.html', {'shipping_form': shipping_form})
    else:
        return redirect('login')

     
def product_detail(request, pk):
    product_instance = Product.objects.get(id=pk)  # Use the correct model 'Product'
    return render(request, 'myapp/product.html', {'product': product_instance})

def index(request):
    products = Product.objects.all()  # Use the correct model 'Product'
    return render(request, 'myapp/index.html', {'products': products})

def about(request):
    return render(request, 'myapp/about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('index')
        else:
            messages.error(request, "Login failed")
            return redirect('login')
    else:
        return render(request, 'myapp/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    form=SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered successfully.")
            return redirect('index') 
        else:
                messages.error(request, "Authentication failed..")
                return redirect('register')
    else:
            return render(request, 'myapp/register.html', {'form': form})
def billing(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()

        # Initialize the shipping form with POST data
        shipping_form = ShippingForm(request.POST)

        if request.user.is_authenticated:
            # Validate the form
            if shipping_form.is_valid():
                # Get cleaned data from the form
                shipping_info = shipping_form.cleaned_data

                # Handle download request
                if 'download' in request.POST:
                    # Generate and return the billing information as a downloadable file
                    response = HttpResponse(content_type='text/plain')
                    response['Content-Disposition'] = 'attachment; filename="billing_info.txt"'

                    # Write billing information to the file
                    response.write(f"Full Name: {shipping_info.get('full_name')}\n")
                    response.write(f"Phone: {shipping_info.get('phone')}\n")
                    response.write(f"Email: {shipping_info.get('email')}\n")
                    response.write(f"Address 1: {shipping_info.get('address_1')}\n")
                    response.write(f"Address 2: {shipping_info.get('address_2')}\n")
                    response.write(f"City: {shipping_info.get('city')}\n")
                    response.write(f"State: {shipping_info.get('state')}\n")
                    response.write(f"Zip Code: {shipping_info.get('zip_code')}\n")
                    response.write(f"Country: {shipping_info.get('country')}\n")
                    response.write(f"Total: ${totals}\n")

                    return response

            # Render the billing page with form errors if the form is invalid
            return render(request, 'payment/billing.html', {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_info": shipping_form.cleaned_data,
                "errors": shipping_form.errors,
            })
        else:
            # Redirect non-authenticated users to the login page
            return redirect('login')

    # Handle GET request (default case)
    return redirect('index')



