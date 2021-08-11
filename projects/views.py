
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Project, Todo
from .forms import TodoChangeStateForm


##### Projects #######

class ProjectListView(ListView):
    """ 
    todo....
    User shall only be able to list 
    projects that they are member of
    """

    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetailView(DetailView):
    """ 
    todo...
    User shall only be able to detailView 
    projects that they are member of
    """
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectCreateView(CreateView):
    """ 
    todo...
    The creator shall be automatic set to the user 
    Only authenticated user shall be able to create a project
    """
    model = Project
    template_name = 'projects/project_create.html'
    fields = ('__all__')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    fields = ('title_project', 'description_project')


###### Todos #######

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'projects/todos/todo_detail.html'


class TodoCreateView(CreateView):
    model = Todo


class TodoDeleteView(DeleteView):
    pass


class TodoUpdateView(UpdateView):
    """
    
    """
    model = Todo
    form_class = TodoChangeStateForm
    template_name = 'projects/todos/todo_update.html'

