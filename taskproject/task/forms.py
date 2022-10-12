from django import forms
from matplotlib import widgets
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'date',)
        labels = {
            "title": "",
            "description": "",
            "date": "",
        }

        widgets = {
            "title" : forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "description" : forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"}),
            "date" : forms.SelectDateWidget(attrs={"class": "form-control", "placeholder": "date"})

        }