from django.contrib import admin
from apps.books.models import *



class AddDeleteViewMixin:
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "date_published"
    list_display = ['title', 'date_published', 'price', 'description']


admin.site.register(Genre)

@admin.register(Author)
class AuthorAdmin(AddDeleteViewMixin, admin.ModelAdmin):
    pass