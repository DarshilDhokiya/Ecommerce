# models.py
from django.db import models
from django.contrib.auth.models import User
from myapp.models import Product

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f'Shipping Address {self.id}'
    
    # order model
class Order(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        full_name = models.CharField(max_length=255)
        email = models.EmailField(max_length=250)
        shipping_address = models.TextField(max_length=15000)
        city = models.CharField(max_length=255)
        amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
        date_ordered = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'Order - {str(self.id)}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Item {self.product.name} (x{self.quantity}) in Order {self.order.id}'
