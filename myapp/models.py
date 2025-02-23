from django.db import models
import datetime

# Create your models here.
class category(models.Model):  # Capitalized 'category' to 'Category'
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class customer(models.Model):  # Capitalized 'customer' to 'Customer'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):  # Correct capitalization for 'Product'
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=10000 ,default='', blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)  # Corrected 'category' to 'Category'
    description = models.CharField(max_length=250, default='', blank=True)  # Fixed typo 'discription' to 'description'
    image = models.ImageField(upload_to='uploads/product')

    def __str__(self):
        return self.name

class order(models.Model):  # Capitalized 'order' to 'Order'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Corrected to 'Product'
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)  # Corrected to 'Customer'
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.product.name} by {self.customer.first_name}"
