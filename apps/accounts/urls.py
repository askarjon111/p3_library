from django.urls import path

from apps.accounts.views import login_user


urlpatterns = [
    path('login/', login_user, name='login')
]

