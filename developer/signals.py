
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
        return developer


def delete_developer(sender, instance, **kwargs):
    instance.user.delete()
