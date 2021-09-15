from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "input-block-level"}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': "input-block-level"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "input-block-level"}))

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise ValidationError("Username already exists")
        if User.objects.filter(username=self.cleaned_data['email']).exists():
            raise ValidationError("Email already exists")

    def save(self):
        user = User.objects.create_user(**self.cleaned_data['user'])
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=153, widget=forms.TextInput(attrs={'class': 'input-block-level'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-block-level'}))

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).first():
            raise ValidationError("user doesn't exists")

        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError(_("Unable login with provided credentials"))
        self.cleaned_data['user'] = user
        return self.cleaned_data
