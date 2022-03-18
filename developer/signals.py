from django.core.mail import send_mail
from django.conf import settings


def create_developer(sender, instance, created, **kwargs):
    from developer.models import Developer
    if created:
        user = instance
        developer = Developer.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name + ' ' + user.last_name,
        )

        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [developer.email],
            fail_silently=False,
        )
        return developer


def update_user(sender, instance, created, **kwargs):
    developer = instance
    user = developer.user
    if created == False:
        user.first_name = developer.name.split(' ')[0]
        user.last_name = developer.name.split(' ')[1]
        user.username = developer.username
        user.email = developer.email
        user.save()


def delete_developer(sender, instance, **kwargs):
    instance.user.delete()
