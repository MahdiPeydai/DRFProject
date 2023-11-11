from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
