from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Category)
