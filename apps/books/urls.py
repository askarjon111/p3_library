from django.urls import path

from apps.books.views import ShopView, IndexView, AboutView, ContactView, BookDetailView, CreateBookView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('book-create/', CreateBookView.as_view(), name='book_create'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]

