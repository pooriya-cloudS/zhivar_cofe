from django.db import models

class Category(models.Model):
    key = models.SlugField(unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='items',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.title
