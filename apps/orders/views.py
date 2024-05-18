from django.shortcuts import redirect

from apps.books.permissions import new_order_permission
from apps.orders.forms import OrderForm

from django.contrib.auth.decorators import login_required


@new_order_permission()
def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        print('get request keldi')
    return redirect('home')
