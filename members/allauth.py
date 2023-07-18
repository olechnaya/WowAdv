from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return '/some/url/'