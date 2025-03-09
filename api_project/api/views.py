from django.shortcuts import render

# Create your views here.
from .serializers import BookSerializers
from .models import Book
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializers
  permission_classes = [IsAdminOrReadOnly]