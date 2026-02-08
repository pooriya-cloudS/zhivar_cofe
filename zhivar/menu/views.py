from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class MenuViewSet(ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        categories = Category.objects.all()
        items = Item.objects.select_related('category').all()

        return Response({
            "categories": CategorySerializer(categories, many=True).data,
            "items": ItemSerializer(items, many=True).data,
        })
