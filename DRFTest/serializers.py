from rest_framework.serializers import ModelSerializer
from .models import *


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['created_at']


