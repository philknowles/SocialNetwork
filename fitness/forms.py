from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    def __int__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset('Exercise',
                 Field(
                     'exercise'
                 ),
                 Field(
                     'weight'
                 ),
                 Field(
                     'reps'
                 ),
            )
        )

#    exercise = forms.CharField(widget=forms.TextInput(
#        attrs={
#            'label': 'Exercise',
#            'class': 'form-control',
#            'placeholder': 'Add an Exercise...',
#            'required': False,
#            'autocomplete': 'off',
#            'form_show_errors': False
#        }
#    ))
#    weight = forms.CharField(widget=forms.TextInput(
#        attrs={
#            'class': 'form-control',
#            'placeholder': 'Add the weight used...',
#            'required': False,
#            'autocomplete': 'off',
#        }
#    ))
#    reps = forms.CharField(widget=forms.TextInput(
#        attrs={
#            'class': 'form-control',
#            'placeholder': 'Add number of reps...',
#            'required': False,
#            'autocomplete': 'off'
#        }
#    ))

    class Meta:
        model = Exercise
        fields = ['exercise', 'weight', 'reps']