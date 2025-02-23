from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library, Author

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()  # Using plain .all() as required
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context