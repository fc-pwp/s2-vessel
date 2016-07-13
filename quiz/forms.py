from django import forms

from .models import Answer
from .models import Question


class StartQuizForm(forms.Form):
    user = forms.CharField(label='당신의 이름은?', max_length=80)


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset=Question.objects.order_by('-seq'))

    class Meta:
        model = Answer
        fields = ('question', 'title', 'number', 'image', 'value', )

