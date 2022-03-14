from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils import search_projects, paginate
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects, search_query = search_projects(request)
    custom_range, projects = paginate(request, projects, 3)

    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    template = 'project/projects.html'
    return render(request, template, context)


def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
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
            form.save()
            return redirect('project:projects')

    context = {'form': form}
    template = 'project/project_form.html'
    return render(request, template, context)


@ login_required(login_url='developer:login')
def update_project(request, pk):
    developer = request.user.developer
    project = developer.project_set.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
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
