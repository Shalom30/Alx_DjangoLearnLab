from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Remove BookList import
from .views import BookList

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),  # Only include the router-generated URLs
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls))
]

