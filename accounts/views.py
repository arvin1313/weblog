from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, LoginForm, ProfileEditForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Profile

def user_register(request):
    if request.user.is_authenticated == True:
        return redirect('blog:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('blog:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('blog:home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('blog:home')


def profile_view(request):
    user = request.user
    profiles = Profile.objects.get(user=user)
    return render(request, 'accounts/profile.html', {'profiles': profiles})


def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_view')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
