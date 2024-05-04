from django.urls import path

from books.views import index_view, book_details, shop_view, about, contact


urlpatterns = [
    path('', index_view, name='home'),
    path('book/<int:pk>/', book_details, name='book_details'),
    path('shop/', shop_view, name='shop'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

