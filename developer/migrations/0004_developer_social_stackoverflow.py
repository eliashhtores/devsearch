# Generated by Django 3.2.10 on 2022-02-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_auto_20220228_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='social_stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
