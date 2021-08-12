
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Project, Todo
from .forms import TodoChangeStateForm, TodoCreateForm


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
    form_class = TodoCreateForm
    template_name = 'projects/todos/todo_create.html'

    # First set the creator to the logged in user
    # Second get the projects pk and link it to the todo
    def form_valid(self, form):
        form.instance.creator_todo = self.request.user
        form.instance.project_id = self.kwargs.get('pk')
        return super().form_valid(form)

    # Get queryset for the project to display information in the template
    # get a context by calling the super() and then get the data with **kwargs
    # then store the data in a list context['project'] and filter the model based on pk 
    def get_context_data(self, **kwargs):
        context = super(TodoCreateView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.filter(pk=self.kwargs.get('pk'))
        return context


class TodoDeleteView(DeleteView):
    pass


class TodoUpdateView(UpdateView):
    """
    
    """
    model = Todo
    form_class = TodoChangeStateForm
    template_name = 'projects/todos/todo_update.html'

