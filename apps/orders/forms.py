from django import forms

from apps.books.models import Book
from apps.orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'name', 'phone_number', 'address', 'city']
