import uuid
from django.db import models
from developer.models import Developer


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(Developer, null=True,
                              blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    UP = 'up'
    DOWN = 'down'

    VOTE_TYPE = (
        (UP, 'Up Vote'),
        (DOWN, 'Down Vote')
    )

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    # Owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project} - {self.value}'


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
