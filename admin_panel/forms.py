from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from admin_panel.models import Recipes


class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'discription', 'image']


class EditRecipeForm(forms.Form):
    name = forms.CharField(label='Назва', max_length=255, required=True)
    description = forms.CharField(label='Опис', max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super(EditRecipeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін', max_length=100, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=True, max_length=100)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'margin-bottom: 10px;'
