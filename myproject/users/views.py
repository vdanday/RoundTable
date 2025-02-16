# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ProfileForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after saving
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form, 'user_role': request.user.role})


def home_view(request):
    return render(request, 'home.html')

def search_view(request):
    query = request.GET.get('skill', '').strip()  # Get the query and strip whitespace

    if query:  # Ensure filtering only happens when query is provided
        users = CustomUser.objects.filter(
            software_skills__icontains=query
        ).order_by('-mentor_score')[:5]
    else:
        users = []  # Return an empty list if query is not provided

    return render(request, 'search.html', {'users': users, 'query': query})


def connect_request_view(request, user_id):
    # Implement connection request logic (e.g., create a Connection model)
    return redirect('home')

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
