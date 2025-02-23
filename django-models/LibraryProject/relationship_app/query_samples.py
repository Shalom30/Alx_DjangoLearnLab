import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Example usage
if __name__ == "__main__":
    # Example: Get books by "J.K. Rowling"
    jk_books = get_books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:", list(jk_books))

    # Example: Get books in "Central Library"
    central_books = get_books_in_library("Central Library")
    print("Books in Central Library:", list(central_books))

    # Example: Get librarian of "Central Library"
    try:
        librarian = get_librarian_for_library("Central Library")
        print("Librarian:", librarian.name)
    except Librarian.DoesNotExist:
        print("No librarian found for this library")