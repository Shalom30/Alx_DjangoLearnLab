from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializers

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializers