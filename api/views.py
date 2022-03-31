from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import Project, Review, Tag


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
    review, created = Review.objects.get_or_create(
        project=project,
        developer=user,
    )

    review.value = data['value']
    review.save()
    project.get_vote_count

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_tag(request):
    tag = Tag.objects.get(pk=request.data['tag_id'])
    project = Project.objects.get(pk=request.data['project_id'])
    project.tags.remove(tag)
    project.save()
    return Response(status='200')
