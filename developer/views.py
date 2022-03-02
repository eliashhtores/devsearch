from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Developer
from .forms import CustomUserCreationForm


def login_user(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('developer:profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('developer:profiles')
        else:
            messages.error(request, 'Invalid credentials')

    template_name = 'developer/login_register.html'
    return render(request, template_name, context)


def logout_user(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('developer:login')


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created')
            login(request, user)
            return redirect('developer:profiles')
        else:
            messages.error(request, 'An error has ocurred during registration')

    page = 'register'
    context = {'page': page, 'form': form}
    template_name = 'developer/login_register.html'
    return render(request, template_name, context)


def profiles(request):
    template_name = 'developer/profiles.html'
    developers = Developer.objects.all()
    context = {'developers': developers}
    return render(request, template_name, context)


def profile(request, pk):
    developer = Developer.objects.get(pk=pk)
    top_skills = developer.skill_set.exclude(description__exact='')
    other_skills = developer.skill_set.filter(description='')[:5]
    context = {'developer': developer,
               'top_skills': top_skills, 'other_skills': other_skills}
    template_name = 'developer/profile.html'
    return render(request, template_name, context)
