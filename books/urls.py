from django.urls import path

from books.views import index_view, book_details, ShopView, IndexView, AboutView, ContactView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('book/<int:pk>/', book_details, name='book_details'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]

