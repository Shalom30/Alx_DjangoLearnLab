from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Author, Library, UserProfile

# Helper function for role checking
def check_role(role):
    def test(user):
        if user.is_authenticated:
            try:
                return user.userprofile.role == role
            except UserProfile.DoesNotExist:
                return False
        return False
    return test

# Existing views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set default role in UserProfile
            UserProfile.objects.filter(user=user).update(role='Member')
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ... keep existing login_view and logout_view unchanged ...

# New role-based views
@login_required
@user_passes_test(check_role('Admin'), login_url='/accounts/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_role('Librarian'), login_url='/accounts/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_role('Member'), login_url='/accounts/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Existing LibraryDetailView remains unchanged
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context