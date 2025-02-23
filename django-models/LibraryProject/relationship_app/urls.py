from django.urls import path
from .views import list_books, LibraryDetailView  # Explicit imports

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Direct reference
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]