import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (corrected)
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # Using OneToOne reverse relation

# Example usage
if __name__ == "__main__":
    try:
        # Example: Get books by "J.K. Rowling"
        rowling_books = get_books_by_author("J.K. Rowling")
        print("Books by Rowling:", [b.title for b in rowling_books])
        
        # Example: Get books in library
        library_books = get_books_in_library("Central Library")
        print("Library books:", [b.title for b in library_books])
        
        # Example: Get librarian
        librarian = get_librarian_for_library("Central Library")
        print("Librarian:", librarian.name if librarian else "None")
        
    except Author.DoesNotExist:
        print("Author not found")
    except Library.DoesNotExist:
        print("Library not found")
    except Exception as e:
        print("Error:", str(e))