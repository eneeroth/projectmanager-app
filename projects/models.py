from django.db import models
from django.conf import settings # datetime
from django.contrib.auth import get_user_model # To referens the custom user model from accounts.CutsomUser
from django.urls import reverse


class Project(models.Model):
    """
    Project is the main model that will display a overview of the project

    todo - 'is_active' checkbox 

    """
    title_project = models.CharField(max_length=50)
    description_project = models.TextField()
    creator_project = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created_project = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(get_user_model(), related_name='members', null=False, blank=False)
    admin = models.ManyToManyField(get_user_model(), related_name='admin', null=False, blank=False)
    #active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_project

    def get_absolute_url(self):
        return reverse("project_list")
    

class Todo(models.Model):
    """
    Todo uses foreignKey to map to the right project, it has three choices in state_todo
    to keep track of the todo
    """
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='todos', null=True)
    title_todo = models.CharField(max_length=50)
    description_todo = models.TextField()
    creator_todo = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    date_created_todo = models.DateTimeField(auto_now_add=True)
    state_todo = models.CharField(choices=[('Planning', 'Planning state'), ('Running', 'Running state'), ('Finished', 'Finnished state'),], default='Planning', max_length=20)

    def __str__(self):
        return self.title_todo

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.project.pk)])


class Comments(models.Model):
    pass


