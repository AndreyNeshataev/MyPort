from django import forms
from django.contrib.auth.forms import AuthenticationForm  #, UserChangeForm UserCreationForm,
from django.contrib.auth.models import User


# class RegisterUserForm(UserCreationForm):
#     username = forms.CharField(label='Логин')
#     first_name = forms.CharField(max_length=30, label='Имя', required=True)
#     password1 = forms.CharField(label='Пароль')
#     password2 = forms.CharField(label='Повтор пароля')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'password1', 'password2')
#
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
