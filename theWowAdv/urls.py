from django.urls import path
from .views import IndexView,\
    AdvDetailView,\
    AdvCreateView,\
    AdvUpdateView,\
    AdvDeleteView

app_name="wow_adv"

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам 
    # у нас останется пустым, позже станет ясно почему
    path('', IndexView.as_view(), name="home"),
    path('advert/<int:pk>', 
         AdvDetailView.as_view(), 
         name="adv-detail"),
    path('create-adv/', 
        AdvCreateView.as_view(), 
        name='create_adv'),
    path('advert/edit/<int:pk>',
        AdvUpdateView.as_view(),
        name='edit_adv'),
    path('advert/<int:pk>/remove',
        AdvDeleteView.as_view(),
        name='remove_adv'),
]
