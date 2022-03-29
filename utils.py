from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from developer.models import Skill, Developer
from project.models import Project, Tag


def search_profile(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(
        name__icontains=search_query)

    developers = Developer.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skills)).order_by('name')
    return developers, search_query


def paginate(request, queryset, results):
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, results)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    left_index = (int(page) - 3) if (int(page) - 3) > 0 else 1
    right_index = (int(page) + 3) if (int(page) +
                                      3) < paginator.num_pages else paginator.num_pages

    custom_range = range(left_index, right_index + 1)
    return custom_range, queryset


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)

    project = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    ).order_by('-vote_ratio', '-vote_total', 'title')
    return project, search_query
