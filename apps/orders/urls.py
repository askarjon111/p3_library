from django.urls import path

from apps.orders.views import new_order


urlpatterns = [
    path('order/<int:pk>/', new_order, name='new_order')
]

