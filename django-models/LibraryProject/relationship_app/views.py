from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Library
from django.contrib.auth.decorators import permission_required

# Function-based views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def register(request):  # Changed from register_view
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
      
      
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def check_admin(user):
    return (
        user.is_authenticated and 
        hasattr(user, 'userprofile') and 
        user.userprofile.role == 'Admin'
    )

@login_required
@user_passes_test(check_admin, login_url='/login/')
def admin_view(request):
    # Add admin-specific context or logic here
    return render(request, 'relationship_app/admin_view.html', {
        'user': request.user
    })
    
# For Librarian View
@login_required
@user_passes_test(check_librarian, login_url='/login/')
def librarian_view(request):
    return render(
        request, 
        'relationship_app/librarian_view.html',  # Explicit template path
        {'user': request.user}
    )

# For Member View
@login_required
@user_passes_test(check_member, login_url='/login/')
def member_view(request):
    books = Book.objects.all()
    return render(
        request,
        'relationship_app/member_view.html',  # Explicit template path
        {
            'user': request.user,
            'books': books
        }
    )
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required  # Fixed import
from .models import Book, Author, Library
from .forms import BookForm

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})