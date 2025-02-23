from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        required=True
    )
    full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        required=True
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True
    )
    address_1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 1'}),
        required=True
    )
    address_2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2'}),
        required=False
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
        required=True
    )
    state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
        required=False
    )
    zip_code = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
        required=False
    )
    country = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
        required=True
    )

    class Meta:
        model = ShippingAddress
        fields = ['phone', 'full_name', 'email', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'country']
        exclude = ['user',]