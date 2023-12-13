from django import forms


class Registration_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input'}))


class Sign_in_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input'}))
