from django import forms
from crispy_forms.helper import FormHelper
from .models import Task


class TaskForm(forms.ModelForm):
    # This definition removes the label for the input field, task_name
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['task_name'].label = False

    helper = FormHelper()

    task_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add a task...'
        }
    ))

    class Meta:
        model = Task
        fields = ('task_name',)