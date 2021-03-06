# Generated by Django 3.2.5 on 2021-08-17 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0013_remove_project_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='admin',
            field=models.ManyToManyField(blank=True, null=True, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
