from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils import search_projects, paginate
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm


def projects(request):
    projects, search_query = search_projects(request)
    custom_range, projects = paginate(request, projects, 6)

    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    template = 'project/projects.html'
    return render(request, template, context)


def project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.developer = request.user.developer
        review.save()
        project.get_vote_count
        messages.success(request, 'Review added successfully!')
        return redirect('project:project', pk=pk)

    context = {'project': project, 'form': form}
    template = 'project/project.html'
    return render(request, template, context)


@ login_required(login_url='developer:login')
def create_project(request):
    developer = request.user.developer
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = developer
            project.save()
            newtags = request.POST.get('newtags', '').replace(',', ' ').split()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('developer:account')

    context = {'form': form}
    template = 'project/project_form.html'
    return render(request, template, context)


@ login_required(login_url='developer:login')
def update_project(request, pk):
    developer = request.user.developer
    project = developer.project_set.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newtags = request.POST.get('newtags', '').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('developer:account')

    context = {'form': form}
    template = 'project/project_form.html'
    return render(request, template, context)


@ login_required(login_url='developer:login')
def delete_project(request, pk):
    developer = request.user.developer
    project = developer.project_set.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project:projects')

    context = {'object': project}
    template = 'delete_template.html'
    return render(request, template, context)
