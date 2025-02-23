from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Book management URLs (updated to match exact requirements)
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    
    # Existing URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),
    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'),
]