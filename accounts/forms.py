from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자, 공백 입력 불가',
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'nickname')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='패스워드', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
