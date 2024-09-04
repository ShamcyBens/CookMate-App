from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('recipe_list')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})


# users/views.py


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('recipe_list')
    else:
        form = AuthenticationForm()
    return render(request, 'Users/login.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')



def index(request):
    if request.method == 'POST':
        # Handle registration logic
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return redirect('index')

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Log the user in
        login(request, user)

        # Redirect to a success page or home page
        return redirect('home')

    # If the request is GET, render the React app
    return render(request, 'index.html')