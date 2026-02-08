from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('key', 'title')


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.key')

    class Meta:
        model = Item
        fields = ('id', 'category', 'title', 'description', 'price', 'image')

    def get_id(self, obj):
        return f"{obj.category.key}-{obj.pk}"
