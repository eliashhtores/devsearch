from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import Project


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/v1/project/'},
        {'GET': 'api/v1/project/id'},
        {'POST': 'api/v1/project/id/vote'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
