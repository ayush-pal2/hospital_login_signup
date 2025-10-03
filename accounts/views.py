from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type'],
                profile_picture=form.cleaned_data['profile_picture'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    profile = request.user.profile
    if profile.user_type == 'patient':
        return render(request, 'accounts/patient_dashboard.html', {'profile': profile})
    elif profile.user_type == 'doctor':
        return render(request, 'accounts/doctor_dashboard.html', {'profile': profile})
