from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import Project


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_vote(request, pk):
    project = Project.objects.get(pk=pk)
    user = request.user.developer
    data = request.data
    print(data)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
