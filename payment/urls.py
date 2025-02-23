# payment/urls.py
from django.urls import path
from . import views

app_name = 'payment'  

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('billing/', views.billing, name='billing'),

]
