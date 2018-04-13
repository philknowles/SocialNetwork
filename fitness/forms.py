from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, ButtonHolder

from .models import Exercise


class ExerciseForm(forms.ModelForm):

    exercise_date = forms.DateField(label='', required=True,
                                    widget=forms.TextInput(attrs={'type': 'date'}))
    exercise = forms.CharField(label='', max_length=255, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Exercise'}))

    weight = forms.CharField(label='', max_length=10, required=False,
                             widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter Weight in Metrics'}))

    reps = forms.CharField(label='', max_length=10, required=False,
                           widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter Total Repetitions'}))

    sets = forms.CharField(label='', max_length=100, required=False,
                           widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter Number of Sets'}))

    def __int__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))

    class Meta:
        model = Exercise
        fields = ['exercise_date', 'exercise', 'weight', 'reps', 'sets', ]
