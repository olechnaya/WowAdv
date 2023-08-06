from django.urls import path
# from allauth.account.views import LoginView, SignupView, LogoutView
from members.views import *

app_name="wow_members"

urlpatterns = [
    # path('login',LoginView.as_view(), name="custom_login" ),
    # path('signup', SignupView.as_view(), name="custom_signup" ),
    # path('logout', LogoutView.as_view(), name="custom_logout" ),
    path('<int:pk>', profile, name="view_profile"),
    path('edit_profile', UserEditView.as_view(), name="edit_profile"),
    path('search/', ResponseSearch.as_view(), name='search'),
    path('approve/<int:pk>', ApproveResponse, name='approve_response'),
    path('reject/<int:pk>', RejectResponse, name='reject_response'),
    path('delete/<int:pk>', DeleteResponse, name='delete_response'),
]