from django import forms
import django_filters as filters
from theWowAdv.models import Advertisement, Response

# создаём фильтр
class ResponseFilter(filters.FilterSet):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ResponseFilter, self).__init__(*args, **kwargs)
        self.filters['advert'].queryset = Advertisement.objects.filter(author=self.user)

    class Meta:
        model = Response
        fields = ['advert']