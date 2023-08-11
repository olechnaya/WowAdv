from django.urls import path
# from allauth.account.views import LoginView, SignupView, LogoutView
from members.views import *
#from django.contrib.auth import views as auth_views

app_name="wow_members"

urlpatterns = [
    # path('login',LoginView.as_view(), name="custom_login" ),
    # path('signup', SignupView.as_view(), name="custom_signup" ),
    # path('logout', LogoutView.as_view(), name="custom_logout" ),
    path('<int:pk>', profile, name="view_profile"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='members/change_password.html')),
    path('password/', PasswordChangeView.as_view(success_url=reverse_lazy('wow_members:password_success'),template_name='members/change_password.html'), name='change_password'),
    path('password_success/', password_success),
    path('search/', ResponseSearch.as_view(), name='search'),
    path('approve/<int:pk>', ApproveResponse, name='approve_response'),
    path('reject/<int:pk>', RejectResponse, name='reject_response'),
    path('delete/<int:pk>', DeleteResponse, name='delete_response'),
]