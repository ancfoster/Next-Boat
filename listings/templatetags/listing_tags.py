from django import template

register = template.Library()
#This filter is from Stackoverflow user artem
#https://stackoverflow.com/questions/8317537/django-templates-split-string-to-array
@register.filter(name='split')
def split(value, arg):
    return value.split("^*")



