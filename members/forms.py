from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import LoginForm
from django.contrib.auth.models import User
from django import forms


class WowAdvLoginForm(LoginForm):
    #required_css_class = 'required'
    #error_css_class = 'error'
    # TODO: нет вывода ошибок, не производится вход ни по логину ни по мейлу. через админ по учетке заходит kozhinova.olka@yandex.ru _Rosenrot1988 ч
    def __init__(self, *args, **kwargs):
        super(WowAdvLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = 'Логин или почта'
        self.fields['login'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'id': 'login' 
        })   
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
))

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=False,max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=False,max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control-plaintext','disabled':'disabled'}))
    is_superuser = forms.CharField(required=False,max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check','disabled':'disabled'}))
    is_staff = forms.CharField(required=False,max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check','disabled':'disabled'}))
    is_active = forms.CharField(required=False,max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check','disabled':'disabled'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control-plaintext','disabled':'disabled'}))

    class Meta:
        model = User
        exclude=('password',)
        fields = ('username','first_name','last_name', 'email', 'date_joined', 'last_login','is_superuser','is_staff','is_active')
