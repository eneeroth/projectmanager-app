from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, Todo

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'projects/todo_detail.html'