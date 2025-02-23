# relationship_app/query_samples.py

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # Exact requested syntax

# Full updated file with context:
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # Exact requested pattern

if __name__ == "__main__":
    try:
        # Test data should match these values
        print("Books by Rowling:", [b.title for b in get_books_by_author("J.K. Rowling")])
        print("Library books:", [b.title for b in get_books_in_library("Central Library")])
        print("Librarian:", get_librarian_for_library("Central Library").name)
        
    except Author.DoesNotExist:
        print("Author not found")
    except Library.DoesNotExist:
        print("Library not found")
    except Librarian.DoesNotExist:
        print("Librarian not found")