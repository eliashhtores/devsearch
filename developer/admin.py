from django.contrib import admin
from .models import Developer, Skill, Message


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'username', 'email', 'short_intro', 'social_github',
                    'social_twitter', 'social_linkedin', 'social_youtube', 'social_website')
    list_filter = ('user', 'name', 'username',)
    search_fields = ('user', 'name', 'username', 'email', 'short_intro', 'social_github',
                     'social_twitter', 'social_linkedin', 'social_youtube', 'social_website')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('developer', 'name', 'description')
    list_filter = ('developer', 'name',)
    search_fields = ('developer', 'name', 'description')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'name', 'email', 'subject')
    list_filter = ('sender', 'receiver', 'name', 'email', 'subject')
    search_fields = ('sender', 'receiver', 'name', 'email', 'subject', 'body')


admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Message, MessageAdmin)
