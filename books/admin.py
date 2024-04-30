from django.contrib import admin
from books.models import *


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
