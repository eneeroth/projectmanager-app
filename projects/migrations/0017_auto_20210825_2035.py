# Generated by Django 3.2.5 on 2021-08-25 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20210825_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_project', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='commenttodo',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_todo', to='projects.todo'),
        ),
    ]
