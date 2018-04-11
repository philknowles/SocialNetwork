from django import forms
from crispy_forms.helper import FormHelper
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    exercise = forms.CharField(widget=forms.TextInput(
        attrs={
            'label': 'Exercise',
            'class': 'form-control',
            'placeholder': 'Add an Exercise...',
            'required': False
        }
    ))
    weight = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add the weight used...',
            'required': False
    }
    ))
    reps = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Add number of reps...',
            'required': False
        }
    ))

    class Meta:
        model = Exercise
        fields = ['exercise', 'weight', 'reps']