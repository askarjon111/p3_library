from django import forms

from books.models import Book
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'name', 'phone_number', 'address', 'city']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        book = Book.objects.get(id=kwargs['pk'])
        self.fields['book'] = book
