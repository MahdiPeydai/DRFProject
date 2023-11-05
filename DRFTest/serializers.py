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
