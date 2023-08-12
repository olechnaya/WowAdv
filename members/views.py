from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from members.forms import EditProfileForm

from theWowAdv.models import Advertisement, Response
from members.filters import ResponseFilter

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('wow_members:password_success')


def password_success(request):
    return render(request, 'members/password_success.html', {})

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'members/profile_edit.html'
    success_url = reverse_lazy('wow_adv:home')

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> User:
        return self.request.user

def UserProfileView(request, pk):
    if request.user.is_authenticated:
        profile = User.objects.get(pk=pk)
        advert_responses = _getUserArdvertResponses(request.user)
        user_adverts = Advertisement.objects.all().filter(author=request.user)
        
        return render(request,"members/profile.html", {
            "profile":profile,
            "adverts": user_adverts,
            "advResponses": advert_responses
        })
    else:
        messages.success(request,('Надо залогиниться'))
        return redirect('home')


class ResponseSearch(ListView):
    model = Response  
    template_name = 'members/response_search.html'
    context_object_name = 'responses'

    def get_queryset(self) -> QuerySet[Any]:
        return Response.objects.filter(advert__author=self.request.user).order_by('-dateCreation') 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(
            self.request.GET,
            user=self.request.user,
            queryset=self.get_queryset()
        ) 
        return context

# TODO: вынести в функцию отправки почты
def _getUserArdvertResponses(user_obj):
    user_adverts = Advertisement.objects.all().filter(author=user_obj)
    advert_ids = user_adverts.values_list('id', flat=True)
    advert_responses = Response.objects.filter(advert__id__in=advert_ids)
    return advert_responses

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL



def ApproveResponse(request, pk): 
    response = Response.objects.get(pk=pk)
    response.isApproved = True
    response.save(update_fields=['isApproved'])
    
    email = response.responseUser.email
    html = render_to_string(
        'mailing/response_status_notification.html', 
        {
            'response': response,
            'user': response.responseUser,
        },
    )
    
    msg = EmailMultiAlternatives(
        subject=f'Ваш отклик принят - {response.title}',
        body='',
        from_email= DEFAULT_FROM_EMAIL,
        to=[email,], # это то же, что и recipients_list - передаем коллекцию
    )
    
    msg.attach_alternative(html, 'text/html')
    try:
        msg.send() # отсылаем  
    except Exception as e:
        print(e)
    return redirect(request.META.get('HTTP_REFERER'))

def RejectResponse(request, pk): 
    response = Response.objects.get(pk=pk)
    response.isApproved = False
    response.save(update_fields=['isApproved']) 

    email = response.responseUser.email
    html = render_to_string(
        'mailing/response_status_notification.html', 
        {
            'response': response,
            'user': response.responseUser,
        },
    )
    
    msg = EmailMultiAlternatives(
        subject=f'Ваш отклик отклонен - {response.title}',
        body='',
        from_email= DEFAULT_FROM_EMAIL,
        to=[email,], # это то же, что и recipients_list - передаем коллекцию
    )
    
    msg.attach_alternative(html, 'text/html')
    try:
        msg.send() # отсылаем  
    except Exception as e:
        print(e)
    return redirect(request.META.get('HTTP_REFERER'))

def DeleteResponse(request, pk):
    response = Response.objects.get(pk=pk)
    response.delete()
    return redirect(request.META.get('HTTP_REFERER'))