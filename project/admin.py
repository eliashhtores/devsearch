from django.contrib import admin
from .models import Project, Review, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created')
    list_filter = ('title', 'owner', 'created')
    search_fields = ('title', 'owner', 'description')
    ordering = ('-created',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'value', 'developer')
    list_filter = ('project', 'value', 'created')
    search_fields = ('project', 'body')
    ordering = ('-created',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_filter = ('name', 'created')
    search_fields = ('name',)
    ordering = ('-created',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
