from django import forms


class StartQuizForm(forms.Form):
    user = forms.CharField(max_length=80)

