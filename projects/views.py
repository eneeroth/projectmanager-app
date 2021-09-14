
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from .models import Project, Todo, CommentProject, CommentTodo
from .forms import TodoUpdateForm, TodoCreateForm, ProjectAddMemberForm, ProjectCreateForm


##### Projects #######

class ProjectListView(LoginRequiredMixin, ListView):
    """ 
    """

    model = Project
    template_name = 'projects/project_list.html'

    # Order the projects by date and filter for the projects the user are a member or admin in
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all().order_by('-date_created_project')
        projects = projects.filter(admin=self.request.user).distinct() | projects.filter(members=self.request.user).exclude(admin=self.request.user).distinct()
        context['projects'] = projects
        print(projects)
        return context

    # # Filter the query to projects user are a member of or admin
    # def get_queryset(self, *args, **kwargs):
    #     return super().get_queryset(*args, **kwargs).filter(admin=self.request.user) | super().get_queryset(*args, **kwargs).filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """ 

    """
    model = Project
    template_name = 'projects/project_detail.html'

    # Filter the comments by date, newest first
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = CommentProject.objects.filter(project=self.kwargs.get('pk')).order_by('-date')
        context['comments'] = comments
        return context

    # Check to see if member or admin of a project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user in obj.members.all() or self.request.user in obj.admin.all() or self.request.user == obj.creator_project:
            return True
        else:
            return False


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """ 
    The creator will be automatic set to the user with form_valid
    Only authenticated are able to create project with loginRequiredMixin
    """
    model = Project
    template_name = 'projects/project_create.html'
    form_class = ProjectCreateForm

    def form_valid(self, form):
        form.instance.creator_project = self.request.user
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('project_list')

    # Check to see if creator or admin of a project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.creator_project or self.request.user in obj.admin.all():
            return True
        else:
            return False


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    fields = ('title_project', 'description_project')

    # Check to see if creator or admin of a project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.creator_project or self.request.user in obj.admin.all():
            return True
        else:
            return False


class ProjectAddMemberView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectAddMemberForm
    template_name = 'projects/project_add_member.html'

    # Check to see if creator or admin of a project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.creator_project or self.request.user in obj.admin.all():
            return True
        else:
            return False


###### Todos #######

class TodoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Todo
    template_name = 'projects/todos/todo_detail.html'   

    # Check to see if creator, admin or member of a project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.project.creator_project or self.request.user in obj.project.admin.all() or self.request.user in obj.project.members.all():
            return True
        else:
            return False


class TodoCreateView(LoginRequiredMixin, CreateView):
    """
    BUG: User can create todo on every project by using the URL
    """
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
    # Filter by pk and run get_object_or_404
    # then store the data in a dict context['project']
    def get_context_data(self, **kwargs):
        context = super(TodoCreateView, self).get_context_data(**kwargs)
        project = Project.objects.filter(pk=self.kwargs.get('pk'))
        get_object_or_404(project)
        context['project'] = project

        return context


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = 'projects/todos/todo_delete.html'

    # Get the todo.project.pk to reverse_lazy on successfully deletion
    def get_success_url(self):
        project = self.object.project

        return reverse_lazy('project_detail', kwargs={'pk': project.pk})

    # Check to see if creator or admin of a project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.project.creator_project or self.request.user in obj.project.admin.all():
            return True
        else:
            return False


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    form_class = TodoUpdateForm
    template_name = 'projects/todos/todo_update.html'

    # Check to see if creator or member of project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.project.creator_project or self.request.user in obj.project.members.all() or self.request.user in obj.project.admin.all():
            return True
        else:
            return False


########### Comments ###########

class CommentProjectView(LoginRequiredMixin, CreateView):
    model = CommentProject
    template_name = 'projects/comments/comment_project_create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.project_id = self.kwargs.get('pk')
        return super().form_valid(form)


class CommentProjectEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CommentProject
    template_name = 'projects/comments/comment_project_edit.html'
    fields = ['title', 'body']

    # Check to see if creator or member of project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.project.creator_project or self.request.user in obj.project.members.all():
            return True
        else:
            return False


class CommentProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentProject
    template_name = 'projects/comments/comment_project_delete.html'

    def get_success_url(self):
        project = self.object.project

        return reverse_lazy('project_detail', kwargs={'pk': project.pk})

    # Check to see if creator or member of project else 403
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.project.creator_project or self.request.user in obj.project.members.all():
            return True
        else:
            return False


class CommentTodoView(CreateView):
    model = CommentTodo
    template_name = 'projects/comments/'


class CommentTodoEditView(UpdateView):
    model = CommentTodo
    template_name = 'projects/comments/'


class CommentTodoDeleteView(DeleteView):
    model = CommentTodo
    template_name = 'projects/comments/'