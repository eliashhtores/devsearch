from django.shortcuts import render


def projects(request):
    msg = 'Hello from the main page'
    return render(request, 'project/projects.html', {'msg': msg})


def project(request, pk):
    return render(request, 'project/single.html')
