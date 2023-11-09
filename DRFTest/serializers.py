from rest_framework import serializers, reverse
from rest_framework.serializers import ModelSerializer
from .models import *


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['created_at']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['created_at']


class AuthorSerializer(ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at']


class BookSerializer(ModelSerializer):

    def get_author_url(self, obj):
        url = serializers.HyperlinkedRelatedField(view_name='AuthorDetail', queryset=Author.objects.all())
        return url.get_url(obj=obj.author, view_name='AuthorDetail', request=self.context['request'], format=None)
    author_url = serializers.SerializerMethodField(method_name='get_author_url')

    def get_publisher_url(self, obj):
        url = serializers.HyperlinkedRelatedField(view_name='PublisherDetail', queryset=Publisher.objects.all())
        return f"{url.get_url(obj=obj.publisher, view_name='PublisherDetail', request=self.context['request'], format=None)}"
    publisher_url = serializers.SerializerMethodField(method_name='get_publisher_url')

    class Meta:
        model = Book
        fields = ['id',
                  'name',
                  'page',
                  'author',
                  'author_url',
                  'publisher',
                  'publisher_url',
                  'categories',
                  'readers',
                  'created_at',
                  'updated_at']
        read_only_fields = ['created_at',
                            'updated_at']
