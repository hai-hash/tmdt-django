from django import template

register = template.Library()
@register.simple_tag
def cal(a,b):
    return a*b