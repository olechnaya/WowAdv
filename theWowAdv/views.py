from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import\
     ListView,\
     DetailView,\
     CreateView,\
     UpdateView,\
     DeleteView


from theWowAdv.models import *
from theWowAdv.forms import AdvertisementForm
from django.conf import settings
from django.urls import reverse_lazy

class IndexView(ListView):
    model = Advertisement
    template_name = "theWow/index.html"
    context_object_name = 'posts'


from django.core.cache import cache # импортируем наш кэш      
class AdvDetailView(DetailView):
    model = Advertisement
    template_name = "theWow/adv_detail.html"
    context_object_name = 'adv'

    def get_object(self, *args, **kwargs): # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}', None) # кэш очень похож на словарь, и метод get действует также. Он забирает значение по ключу, если его нет, то забирает None.
 
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset) 
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        
        return obj

class AdvCreateView(LoginRequiredMixin, CreateView):
    #permission_required = ('wow_adv.add_post')
    template_name = 'theWow/adv_create.html'
    form_class = AdvertisementForm
    login_url = settings.LOGIN_URL

    # def handle_no_permission(self):        
    #     # add custom message
    #     messages.error(self.request, 'Чтобы редактировать объявление, вам нужно войти в качестве автора')
    #     return redirect(self.request.get_full_path(),self.get_login_url())


# проверка на то, что редактирует её создатель или админ, а не какой либо другой автор 
# дженерик для редактирования объекта
class AdvUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'theWow/adv_create.html'
    form_class = AdvertisementForm
    login_url = settings.LOGIN_URL

    # # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Advertisement.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['isUpdateView'] = True        
        return context
    
class AdvDeleteView(LoginRequiredMixin,DeleteView):
    #permission_required = ('news.delete_post')
    template_name = 'theWow/adv_delete.html'
    queryset = Advertisement.objects.all()
    # success_url = '/'
    success_url = reverse_lazy('wow_adv:home')
    login_url = settings.LOGIN_URL
    #redirect_field_name = 'redirect_to'
    
    # def handle_no_permission(self):        
    #     # add custom message
    #     messages.error(self.request, 'Чтобы удалить статью, вам нужно войти в качестве автора')
    #     return redirect(self.get_login_url())