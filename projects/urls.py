from django.urls import path

from .views import ProjectListView, ProjectDetailView, TodoDetailView


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
]