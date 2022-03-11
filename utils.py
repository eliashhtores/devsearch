from django.db.models import Q
from developer.models import Skill, Developer
from project.models import Project, Tag


def search_profile(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    developers = Developer.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skills))
    return developers, search_query


def search_project(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    project = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query)).order_by('-created')
    return project, search_query
