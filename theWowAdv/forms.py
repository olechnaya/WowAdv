from django import forms
from django.forms import ModelForm

from bootstrap_datepicker_plus.widgets import DateTimePickerInput


from theWowAdv.models import *

class AdvertisementForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = Advertisement
        fields = ['title', 'category', 'body', 'exp_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            # 'body': forms.Textarea(attrs={'class':'form-control'}),
            'exp_date': DateTimePickerInput(options={"format": "DD/MM/YYYY"}),
        }

        # labels = {
        #     'title' : 'Заголовок поста',
        #     'text' : 'Текст поста',
        #     'author': 'Выбираем автора',
        #     'category': 'Выбираем категорию',
        #     'postType': 'Выбираем тип'
        # }