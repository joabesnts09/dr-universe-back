from rest_framework import serializers
from .models import Articles


class BulkArticlesSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        articles = [Articles(**item) for item in validated_data]
        return Articles.objects.bulk_create(articles)

class ArticlesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Articles
        fields = '__all__'
        list_serializer_class = BulkArticlesSerializer


    def create(self, validated_data):
        return Articles.objects.create(**validated_data)