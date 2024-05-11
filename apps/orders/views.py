from django.shortcuts import redirect, render

from apps.books.models import Book
from apps.orders.forms import OrderForm



def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('test')

    else:
        print('get request keldi')
    return redirect('home')
