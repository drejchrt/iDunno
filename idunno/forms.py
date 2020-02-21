from django import forms
from .models import Question

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','hint3','hint2','hint1','answer','color')
