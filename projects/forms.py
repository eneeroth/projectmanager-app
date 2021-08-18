from django import forms

from django.forms import ModelForm
from django.forms.widgets import Select

from .models import Todo, Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title_project', 'description_project', 'admin', 'members',)

        widgets = {
            'admin': forms.SelectMultiple(),
            'members': forms.SelectMultiple(),
            }
        
        help_texts = {
            'admin': 'To select multiple press "Ctrl"',
            'members': 'To select multiple press "Ctrl"'
        }

        


class ProjectAddMemberForm(ModelForm):
    class Meta:
        model = Project
        fields = ('members',)

        widgets = {
            'members': forms.CheckboxSelectMultiple(),
            }

        labels = {
            'members': '',
            }


class TodoCreateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title_todo', 'description_todo')

        widgets = {
            'title_todo': forms.TextInput(attrs={'cols': 5, 'rows': 1}),
            'description_todo': forms.Textarea(attrs={'cols': 4, 'rows': 4})
        }


class TodoUpdateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('state_todo', 'title_todo', 'description_todo',)

        widgets = {
            'description_todo': forms.Textarea(attrs={'cols': 5, 'rows': 5})
        }



