from django import forms


class UserForms(forms.Form):
    name = forms.CharField(required=True,label='Имя',widget = forms.TextInput(attrs={'class':'myclass'}))
    age = forms.IntegerField(required=False)
    # email = forms.EmailField(widget=forms.EmailInput(attrs={class= 'class'})
    required_css_class = 'myclass'