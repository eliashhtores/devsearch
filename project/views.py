from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project/projects.html', context)


def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project/project.html', context)


@login_required(login_url='developer:login')
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project:projects')

    context = {'form': form}
    template = 'project/project_form.html'
    return render(request, template, context)


@login_required(login_url='developer:login')
def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project:projects')

    context = {'form': form}
    template = 'project/project_form.html'
    return render(request, template, context)


@login_required(login_url='developer:login')
def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project:projects')

    context = {'object': project}
    template = 'project/delete_template.html'
    return render(request, template, context)
