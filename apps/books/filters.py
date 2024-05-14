from django_filters import FilterSet

from apps.books.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {'title': ['contains'], 'price': ['lte'], 'authors': ['exact'], 'genres': ['exact']}
