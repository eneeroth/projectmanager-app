from django.contrib import admin

from .models import Project, Todo, CommentProject, CommentTodo


class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0


class CommentProjectInline(admin.TabularInline):
    model = CommentProject
    extra = 1


class CommentTodoInline(admin.TabularInline):
    model = CommentTodo
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        TodoInline,
        CommentProjectInline,
    ]


class TodoAdmin(admin.ModelAdmin):
    inlines = [
        CommentTodoInline,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Todo, TodoAdmin)

