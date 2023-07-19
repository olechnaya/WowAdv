from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView

from theWowAdv.models import Advertisement, Response
from members.filters import ResponseFilter



def profile(request, pk):
    if request.user.is_authenticated:
        profile = User.objects.get(pk=pk)
        # adverts = list(Advertisement.objects.all().filter(author=request.user))
        user_adverts = Advertisement.objects.all().filter(author=request.user)
        advert_ids = user_adverts.values_list('id', flat=True)
        advert_responses = Response.objects.filter(advert__id__in=advert_ids)
        
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
    queryset = Response.objects.order_by('-dateCreation') 
    
    def get_context_data(self, **kwargs): 
        user_adverts = Advertisement.objects.all().filter(author=self.request.user)
        advert_ids = user_adverts.values_list('id', flat=True)
        
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET,
                                            user=self.request.user, 
                                            queryset=Response.objects.filter(advert__id__in=advert_ids)
        ) 
        return context