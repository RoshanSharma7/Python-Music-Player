from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SongForm
from .models import Song

# Create your views here.
# Register views

def register_view(request):
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = "Please fix the errors below."
    else:
        form = RegisterForm()
    return render(request, 'player/register.html', {'form': form, 'error': error})

# login views

def login_view(request):
    error = None
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            error = "Invalid username or password"
    else:
        form = AuthenticationForm()
    return render(request, 'player/login.html', {'form': form, 'error': error})

# Logout view

def logout_view(request):
    logout(request)
    return redirect('login')

# Song uploading Views

@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.uploaded_by = request.user
            song.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'player/upload.html', {'form': form})

# Home views 

def home(request):
    songs = Song.objects.all()
    return render(request, 'player/home.html', {'songs': songs})



