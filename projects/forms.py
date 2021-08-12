from django import forms

from django.forms import ModelForm

from .models import Todo, Project


# class ProjectCreateForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ('')

#         widgets = {
#             'title_project': forms.CharField(attrs={'cols': 10, 'rows': 5}),
#             'description_project': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
#             'description_project': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
#             'description_project': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
#         }

class TodoCreateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title_todo', 'description_todo')

        widgets = {
            'title_todo': forms.TextInput(attrs={'cols': 5, 'rows': 1}),
            'description_todo': forms.Textarea(attrs={'cols': 4, 'rows': 4})
        }


class TodoChangeStateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('state_todo', 'title_todo', 'description_todo',)

        widgets = {
            'description_todo': forms.Textarea(attrs={'cols': 5, 'rows': 5})
        }



