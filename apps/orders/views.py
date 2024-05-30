from django.shortcuts import redirect

from apps.books.permissions import new_order_permission
from apps.orders.forms import OrderForm

import telegram

bot = telegram.Bot(token='5553199462:AAEjbZue5IxQXlvRSAOavECU2vUMUCe3vpY')

@new_order_permission()
def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            bot.sendMessage(358554824, f"Yangi zakaz {form.cleaned_data.get('phone_number')}")
        else:
            print(form.errors)
    else:
        print('get request keldi')
    return redirect('home')
