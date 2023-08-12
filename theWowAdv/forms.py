from django import forms
from django.forms import ModelForm



from theWowAdv.models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class AdvertisementForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = Advertisement
        fields = ('title', 'category', 'body', 'exp_date', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'author': forms.TextInput(attrs={'id':'author_id','type':'hidden'}),
            # 'body': forms.Textarea(attrs={'class':'form-control'}),
            'exp_date': DateInput(attrs={'class':'form-control'}),
        }
class ResponseForm(forms.ModelForm):
     class Meta:
        model = Response
        fields = ('title', 'text', 'advert', 'responseUser')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'advert': forms.HiddenInput(),
            'responseUser': forms.HiddenInput(),
        }


class SubscriptionForm(ModelForm):   
    class Meta:
        model = CategorySubscription
        fields = ('name', 'user')

    # CATEGORIES = [
    #     ('T','Танки'),
    #     ('HM','Хилы'),
    #     ('DD','ДД'),
    #     ('TrM','Торговцы'),
    #     ('GM','Гилдмастеры'),
    #     ('QG','Квестгиверы'),
    #     ('FM','Кузнецы'),
    #     ('LM','Кожевники'),
    #     ('PM','Зельевары'),
    #     ('WM','Мастера заклинаний'),
    # ]

    # cats = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #         choices=CATEGORIES, 
    #         label="Категории",) 