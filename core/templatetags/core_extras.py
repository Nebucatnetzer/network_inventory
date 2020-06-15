from django import template

register = template.Library()


@register.filter
def verbose_name(instance):
    return instance._meta.verbose_name
