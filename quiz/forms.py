from django import forms
from .models import Answer, Question

class QuizForm(forms.Form):
    title = forms.CharField(label='질문', max_length=255, min_length=3)
    status = forms.CharField(label='상태', max_length=5)

class StartQuizForm(forms.Form):
    user = forms.CharField(label='당신의 이름은:', max_length=80, min_length=2)

class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset=Question.objects.order_by('-seq'))

    class Meta:
        model = Answer
        fields = ('question', 'content', 'number', 'image', 'value')
