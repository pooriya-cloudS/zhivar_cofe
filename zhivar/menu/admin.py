from django.contrib import admin
from .models import Category, Item
from django.contrib.auth.models import User, Group


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('key', 'title')
    search_fields = ('key', 'title')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    search_fields = ('title', 'description')
    list_filter = ('category',)

admin.site.unregister(User)
admin.site.unregister(Group)

