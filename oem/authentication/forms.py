from django import forms


class NameForm(forms.Form):
    username = forms.CharField(label='Roll number', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class ChangePassword(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())