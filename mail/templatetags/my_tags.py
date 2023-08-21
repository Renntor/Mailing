from django import template

register = template.Library()

@register.filter(name='mediapath')
def media_filter(text):
    return f'/media/{text}'