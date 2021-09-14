from django.urls import path

from .views import *


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    #Projects
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/members/add', ProjectAddMemberView.as_view(), name='project_add_member'),
    #Todos
    path('<int:pk>/todo/create/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/detail/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    #Comments
    path('<int:pk>/comment/', CommentProjectView.as_view(), name='comment_project'),
    path('comment/<int:pk>/edit/', CommentProjectEditView.as_view(), name='comment_project_edit'),
    path('comment/<int:pk>/delete/', CommentProjectDeleteView.as_view(), name='comment_project_delete'),
]