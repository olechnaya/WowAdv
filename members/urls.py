from django.urls import path
# from allauth.account.views import LoginView, SignupView, LogoutView
from members.views import *

app_name="wow_members"

urlpatterns = [
    # path('login',LoginView.as_view(), name="custom_login" ),
    # path('signup', SignupView.as_view(), name="custom_signup" ),
    # path('logout', LogoutView.as_view(), name="custom_logout" ),
    path('<int:pk>', profile, name="view_profile"),
    path('search/', ResponseSearch.as_view(), name='search'),
]