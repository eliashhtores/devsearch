# Generated by Django 3.2.10 on 2022-05-18 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20220316_1216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio']},
        ),
    ]
