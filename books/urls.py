from django.urls import path

from books.views import index_view, book_details


urlpatterns = [
    path('', index_view, name='home'),
    path('book/<int:pk>/', book_details, name='book_details')
]

