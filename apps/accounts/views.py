from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib import messages
from django.urls import reverse_lazy


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            messages.add_message(request, messages.WARNING, "Parol yoki username noto'g'ri")


    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.WARNING, form.errors)
    return render(request, 'register.html', {'form': form})


# Authentication
# Authorisation
# Permission