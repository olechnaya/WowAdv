from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.generic import\
     ListView,\
     DetailView,\
     CreateView,\
     UpdateView,\
     DeleteView


from theWowAdv.models import *
from theWowAdv.forms import AdvertisementForm, ResponseForm, SubscriptionForm
from django.conf import settings



class IndexView(ListView):
    model = Advertisement
    template_name = "theWow/index.html"
    queryset = Advertisement.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
    

from django.views.generic.edit import FormMixin
from django.urls import reverse
class AdvDetailView(FormMixin,DetailView):
    model = Advertisement
    template_name = "theWow/view_adv.html"
    context_object_name = 'adv'
    form_class=ResponseForm

    def get_success_url(self):
        return reverse('wow_adv:view_adv', kwargs={'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(AdvDetailView, self).get_context_data(**kwargs)
        context['form'] = ResponseForm(initial={'advert': self.object, 'responseUser':self.request.user})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(AdvDetailView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)       
    #     context['form'] = self.form     
    #     return context


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
    model = Advertisement
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


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

# TODO: вынести в сигналы
def notify_adv_creator_about_response_added(
        sender, 
        instance, 
        created, 
        **kwargs):
    
    how_to_appeal = "{pronoun},".format(pronoun="Уважаемый пользователь" if instance.responseUser.first_name == "" else instance.responseUser.first_name)
    subject = f'{how_to_appeal}, добавлен отлкик к объявлению {instance.dateCreation.strftime("%d %m %Y")}'

    email = instance.advert.author.email
    html = render_to_string(
        'mailing/notify_adv_creator_about_response_added.html', 
        {
            'response': instance,
            'user': instance.responseUser,
        },
    )
    
    msg = EmailMultiAlternatives(
        subject=subject,
        # subject=f'Добавлен отклик к вашему объявлению - {instance.title}',
        body='',
        from_email= DEFAULT_FROM_EMAIL,
        to=[email,], # это то же, что и recipients_list - передаем коллекцию
    )
    
    msg.attach_alternative(html, 'text/html')
    try:
        msg.send() # отсылаем  
    except Exception as e:
        print(e)

# коннектим наш сигнал к функции обработчику и указываем, к какой именно модели после сохранения привязать функцию
post_save.connect(notify_adv_creator_about_response_added, sender=Response)

# class ResponseCreateView(CreateView):
#     model = Response
#     form_class = ResponseForm
#     template_name = 'theWow/response_create.html'
        
#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         form.instance.advert_id = self.kwargs['pk']
#         form.instance.responseUser = self.request.user
#         return super().form_valid(form)

from django.contrib.auth import get_user_model
def subscribe(request):
    if request.method == 'POST':
        name=request.POST.get('name',None)
        email=request.POST.get('email',None)

        if not name or not email:
            messages.error(request, 'Необходимо предоставить корректный email и имя')
            return redirect('/')
        
        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f'Пользователь с данным email {email} уже зарегистрирован,\
                           вам необходимо залогиниться для подписки / отписки от новостей')
            return redirect(request.META.get('HTTP_REFERER'),'/')
        
        newsletter_subscribed_user = NewsLetterSubscribedUsers.objects.filter(email=email).first()
        if newsletter_subscribed_user:
            messages.error(request, f'Пользователь с данным email {email} уже подписан на наши новости')
            return redirect(request.META.get('HTTP_REFERER'),'/')

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request,e.messages[0])
            return redirect('/')
        
        newsletter_subscribed_user = NewsLetterSubscribedUsers()
        newsletter_subscribed_user.name = name
        newsletter_subscribed_user.email = email
        newsletter_subscribed_user.save()
        messages.success(request, f'{email} успешно подписан на нашу новостную рассылку')
        return redirect(request.META.get('HTTP_REFERER'),'/')