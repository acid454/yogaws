from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


#
# Source: https://ordinarycoders.com/blog/article/django-user-register-login-logout
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Пользователь"
        self.fields['email'].label = "E-mail"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Подтверждение"
        for k in self.fields.keys():
            self.fields[k].help_text = ""
        
        #print(dir(self.fields['username']))
        #self.fields['username'].initial = "test1"
        #self.fields['email'].initial = "test1@mail.com"
        #self.fields['password1'].initial = "test1"
        #self.fields['password2'].initial = "test1"

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Пользователь"
        self.fields['password'].label = "Пароль"

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password',
        }
    ))
