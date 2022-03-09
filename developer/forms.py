from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Developer, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = [
            'name', 'email', 'username', 'location', 'bio', 'short_intro',
            'profile_image', 'social_github', 'social_twitter', 'social_linkedin',
            'social_youtube', 'social_website'
        ]

    def __init__(self, *args, **kwargs):
        super(DeveloperForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
