from typing import Any
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView

from books.models import Book, Genre
from orders.forms import OrderForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['on_trend'] = Book.objects.filter(on_trend=True)
        context['top_books'] = Book.objects.all().annotate(
            order_count=Count('orders')
        ).order_by('order_count')
        context['genres'] = Genre.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book-details.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(initial={'book': context['book']})
        field = context['form'].fields['book']
        field.widget = field.hidden_widget()
        return context


class ShopView(ListView):
    model = Book
    template_name = 'shop.html'
    context_object_name = 'books'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'