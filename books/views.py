from django.shortcuts import render
from books.models import Book
from orders.forms import OrderForm


def index_view(request):
    books_on_trend = Book.objects.filter(on_trend=True)
    return render(request, 'index.html', {'on_trend': books_on_trend})


def book_details(request, pk):
    book = Book.objects.get(id=pk)
    form = OrderForm()
    return render(request, 'book-details.html', {'book': book, 'form': form})
