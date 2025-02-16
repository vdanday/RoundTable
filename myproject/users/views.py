# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ProfileForm
from .models import CustomUser

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

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')


def search_view(request):
    query = request.GET.get('skill')
    users = CustomUser.objects.filter(
        software_skills__icontains=query
    ).order_by('-mentor_score')[:5]
    return render(request, 'search.html', {'users': users, 'query': query})

def connect_request_view(request, user_id):
    # Implement connection request logic (e.g., create a Connection model)
    return redirect('home')
