from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    register  # Make sure this matches your view name
)

urlpatterns = [
    # Book and library views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views
    path('register/', register, name='register'),  # Direct reference
    path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),
    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'),
    path('register/', register, name='register'),
]

from django.urls import path
from .views import register  # Not register_view

urlpatterns = [
    # ... other paths
    
]