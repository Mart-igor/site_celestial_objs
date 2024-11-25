from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
            return HttpResponseRedirect(reverse('main:category_list'))  
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', context={'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login')) 


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user = form.instance
            login(request, user)
            messages.success(request, f'{user.username}, Successful Registration')
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, isinstance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was changed')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})