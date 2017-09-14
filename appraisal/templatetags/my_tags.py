__author__ = 'waqarali'
from django import template
register = template.Library()


@register.inclusion_tag('logged_in/user.html')
def logged_in_user(user, takes_context=True):
    return {'user': user}