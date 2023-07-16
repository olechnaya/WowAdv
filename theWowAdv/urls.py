from django.urls import path
from .views import IndexView, AdvDetailView

app_name="wow_adv"

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам 
    # у нас останется пустым, позже станет ясно почему
    path('', IndexView.as_view(), name="home"),
    path('advert/<int:pk>', 
         AdvDetailView.as_view(), 
         name="advert-detail"),
]