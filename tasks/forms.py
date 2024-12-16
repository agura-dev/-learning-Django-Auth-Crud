#from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title for the task'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the task description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'})
        }