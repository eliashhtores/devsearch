def create_developer(sender, instance, created, **kwargs):
    if created:
        Developer.objects.create(user=instance)


# def developer_deleted(sender, instance, **kwargs):
#     print('Deletion signal sent!')
