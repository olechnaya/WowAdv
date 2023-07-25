from django import template
from theWowAdv.models import Response

register = template.Library()

# не доделано и нигде не используется 
# @register.filter(name='isApproved')
# def get_approved_responses(queryset, key):
#     approvedResponses =  Response.objects.all()
#     return approvedResponses in user.groups.all()