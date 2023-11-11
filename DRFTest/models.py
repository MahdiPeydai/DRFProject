from django.db import models
from slugify import slugify
from django.contrib.auth.models import User


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField('auth.User', related_name='author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, db_collation='utf8_persian_ci', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.user.first_name} {self.user.last_name}", separator='_', allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, db_collation='utf8_persian_ci', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, separator='_', allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, db_collation='utf8_persian_ci', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, separator='_', allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='books')
    readers = models.ManyToManyField('auth.User', related_name='books')
    page = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, db_collation='utf8_persian_ci', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, separator='_', allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"{self.name}"

