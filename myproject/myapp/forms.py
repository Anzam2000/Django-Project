# myapp/forms.py

from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea)