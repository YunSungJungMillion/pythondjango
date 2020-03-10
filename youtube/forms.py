# 폼만드는 방법을 여기에 적을것이다.

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label = 'Your Name',max_length = 20)
    password = forms.CharField(label = 'Your Password',max_length = 20)