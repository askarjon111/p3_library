from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView, ListView

from books.models import Book, Genre
from orders.forms import OrderForm


def index_view(request):
    books_on_trend = Book.objects.filter(on_trend=True)
    top_books = Book.objects.all().annotate(
        order_count=Count('orders')
    ).order_by('order_count')
    genres = Genre.objects.all()

    return render(request, 'index.html', {'on_trend': books_on_trend, 'top_books': top_books, 'genres': genres})


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


def book_details(request, pk):
    book = Book.objects.get(id=pk)
    form = OrderForm(initial={'book': book})
    field = form.fields['book']
    field.widget = field.hidden_widget()
    return render(request, 'book-details.html', {'book': book, 'form': form})


class ShopView(ListView):
    model = Book
    template_name = 'shop.html'
    context_object_name = 'books'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'