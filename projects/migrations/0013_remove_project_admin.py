# Generated by Django 3.2.5 on 2021-08-17 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_project_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='admin',
        ),
    ]
