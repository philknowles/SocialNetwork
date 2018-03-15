from django import forms
from crispy_forms.helper import FormHelper
from .models import Task


class TaskForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    task_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add a task...'
        }
    ))

    class Meta:
        model = Task
        fields = ('task_name',)