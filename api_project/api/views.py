from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializers
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAdminOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializers
  permission_classes = [IsAuthenticated]