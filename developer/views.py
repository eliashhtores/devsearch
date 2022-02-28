from re import template
from django.shortcuts import render
from .models import Developer


def profiles(request):
    template_name = 'developer/profiles.html'
    developers = Developer.objects.all()
    context = {'developers': developers}
    return render(request, template_name, context)


def profile(request, pk):
    developer = Developer.objects.get(pk=pk)
    top_skills = developer.skill_set.exclude(description__exact='')
    other_skills = developer.skill_set.filter(description='')
    context = {'developer': developer,
               'top_skills': top_skills, 'other_skills': other_skills}
    template_name = 'developer/profile.html'
    return render(request, template_name, context)
