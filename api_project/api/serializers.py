from .models import Book 
from rest_framework import serializers

class BookSerializers(serializers.ModelSerializer):
  class Metal:
    model = Book
    field  = '__all__'