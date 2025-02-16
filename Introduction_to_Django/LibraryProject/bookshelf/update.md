#update the publication year of the book
book = Book.objects.get(id=1)
book.title = "Nineteen Eghty-Four"  # Corrected publication year
book.save()  # Save changes to the database

#verify the update
updated_book = Book.objects.get(id=1)
print(updated_book.publication_year)  # Output: Nineteen Eighty-Four