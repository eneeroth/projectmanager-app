from django.urls import path

from .views import (ProjectListView, ProjectDetailView, TodoUpdateView, TodoDetailView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView, TodoCreateView)


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    #Projects
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    #Todos
    path('<int:pk>/todo/create/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/detail/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
]