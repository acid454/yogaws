from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from . import models
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
import os, sys
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, "yoga/containers"))
from integer_constants import VoiceActing, ShavasanaActing, MetronomeTicks


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

    class Meta(UserCreationForm.Meta):
        model = models.User
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

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("kegel_timer", "voice_acting", "shavasana_acting", "metronome")
    
    kegel_timer = forms.BooleanField(label="Включить упражнения Кегеля (если есть в тренировке)", required=False)
    voice_acting = forms.ChoiceField(label="Режим озвучивания", required=False, choices = (
            (VoiceActing.FULL,               "Полный"),
            (VoiceActing.NO_COMMON_COMMENTS, "Без общих комментариев"),
            (VoiceActing.NO_ANY_COMMENTS,    "Без комментариев и описаний"),
            (VoiceActing.ASANA_START_STOP,   "Названия асан и выходы"),
            (VoiceActing.ASANA_NAME_ONLY,    "Только названия асан"),
        )
    )
    shavasana_acting = forms.ChoiceField(label="Озвучивание Шавасаны", required=False, choices = (
            (0, "Согласно общим настройкам"),
            (1, "Всегда озвучивать"),
            (2, "Никогда не озвучивать")
        )
    )
    metronome = forms.ChoiceField(label="Метроном", required=False, choices = (
            (0, "Полный"),
            (1, "Только переходы"),
            (2, "Выключен")
        )
    )
