from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils import search_profile, paginate
from .models import Developer, Message
from .forms import CustomUserCreationForm, DeveloperForm, SkillForm


def login_user(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('developer:account')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'developer:account')
        else:
            messages.error(request, 'Invalid credentials')

    template_name = 'developer/login_register.html'
    return render(request, template_name, context)


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out')
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
            return redirect('developer:edit_account')

    page = 'register'
    context = {'page': page, 'form': form}
    template_name = 'developer/login_register.html'
    return render(request, template_name, context)


def profiles(request):
    developers, search_query = search_profile(request)
    custom_range, developers = paginate(request, developers, 3)

    template_name = 'developer/profiles.html'
    context = {'developers': developers,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, template_name, context)


def profile(request, pk):
    developer = Developer.objects.get(pk=pk)
    top_skills = developer.skill_set.exclude(description__exact='')
    other_skills = developer.skill_set.filter(description='')[:5]
    context = {'developer': developer,
               'top_skills': top_skills, 'other_skills': other_skills}
    template_name = 'developer/profile.html'
    return render(request, template_name, context)


@login_required(login_url='developer:login')
def account(request):
    developer = request.user.developer
    skills = developer.skill_set.all
    context = {'developer': developer, 'skills': skills}
    template_name = 'developer/account.html'
    return render(request, template_name, context)


@login_required(login_url='developer:login')
def edit_account(request):
    form = DeveloperForm(instance=request.user.developer)
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES,
                             instance=request.user.developer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was updated')
            return redirect('developer:account')

    context = {'form': form}
    template_name = 'developer/edit_account.html'
    return render(request, template_name, context)


@login_required(login_url='developer:login')
def create_skill(request):
    form = SkillForm()
    developer = request.user.developer
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.developer = developer
            skill.save()
            messages.success(request, 'Skill was created')
            return redirect('developer:account')

    context = {'form': form}
    template_name = 'developer/skill_form.html'
    return render(request, template_name, context)


@login_required(login_url='developer:login')
def edit_skill(request, pk):
    developer = request.user.developer
    skill = developer.skill_set.get(pk=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            skill.save()
            messages.success(request, 'Skill was updated')
            return redirect('developer:account')

    context = {'form': form}
    template_name = 'developer/skill_form.html'
    return render(request, template_name, context)


@login_required(login_url='developer:login')
def delete_skill(request, pk):
    developer = request.user.developer
    skill = developer.skill_set.get(pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted')
        return redirect('developer:account')
    context = {'object': skill}
    template_name = 'delete_template.html'
    return render(request, template_name, context)


@login_required(login_url='developer:login')
def inbox(request):
    developer = request.user.developer
    messages_received = developer.messages.all()
    unread_count = messages_received.filter(is_read=False).count()
    context = {'messages_received': messages_received,
               'unread_count': unread_count}
    template_name = 'developer/inbox.html'
    return render(request, template_name, context)
