from django.urls import path
from allauth.account.views import LoginView, SignupView
# from theWowAdv.views import

app_name="wow_members"

urlpatterns = [
    path('login',LoginView.as_view(), name="custom_login" ),
    path('signup', SignupView.as_view(), name="custom_signup" ),
    # path('<int:pk>', views.profile, name="index"),
]