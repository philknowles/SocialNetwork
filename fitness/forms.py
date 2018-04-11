from django import forms
from crispy_forms.helper import FormHelper
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    exercise = forms.CharField(label="Exercise", required=True)
    weight = forms.CharField(label="Weight", required=False)
    reps = forms.CharField(label="Reps", required=False)

    helper = FormHelper()
    helper.form_method = 'POST'

    class Meta:
        model = Exercise
        fields = ['exercise', 'weight', 'reps']