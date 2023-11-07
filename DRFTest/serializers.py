from rest_framework import serializers
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
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at']


class BookSerializer(ModelSerializer):
    author = serializers.StringRelatedField()
    author_url = serializers.HyperlinkedRelatedField(
        view_name='AuthorDetail',
        queryset=Author.objects.all()
    )
    publisher = serializers.StringRelatedField()
    publisher_url = serializers.HyperlinkedRelatedField(
        view_name='PublisherDetail',
        queryset=Publisher.objects.all()
    )
    categories = serializers.StringRelatedField(many=True)
    categories_url = serializers.HyperlinkedRelatedField(
        view_name='CategoryDetail',
        queryset=Category.objects.all(),
        many=True
    )
    readers = serializers.StringRelatedField()

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
                  'categories_url',
                  'readers',
                  'created_at',
                  'updated_at']
        read_only_fields = ['created_at',
                            'updated_at']
