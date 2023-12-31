from django.urls import path
from theWowAdv.views import IndexView,\
    AdvDetailView,\
    AdvCreateView,\
    AdvUpdateView,\
    AdvDeleteView,\
    subscribe

app_name="wow_adv"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('advert/<int:pk>', AdvDetailView.as_view(), name="view_adv"),
    path('create-adv/', AdvCreateView.as_view(), name='create_adv'),
    path('advert/edit/<int:pk>', AdvUpdateView.as_view(), name='edit_adv'),
    path('advert/remove/<int:pk>', AdvDeleteView.as_view(), name='remove_adv'),
    path('subscribe', subscribe, name='subscribe'),
    # path('advert/<int:pk>/response', ResponseCreateView.as_view(), name="create_response"),
]
