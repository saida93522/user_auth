from django.contrib.auth import get_user_model
from django import forms

User = get_user_model

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"my_username",
            "id":"floatingInputUsername"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Password",
            "id":"floatingPassword"}
    ))



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"my_username",
            "id":"floatingInputUsername"}   
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"form-control",
            "placeholder":"Password",
            "id":"floatingPassword"}
    ))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(Username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('Invalid username, please enter valid username.')