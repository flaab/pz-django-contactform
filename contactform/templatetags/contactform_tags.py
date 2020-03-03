from django.utils.safestring import mark_safe
from django.apps import apps
from django import template

# Register
register = template.Library()

@register.simple_tag
def app_attr(name):
    """ Returns an attribute from the apps library to the template """
    return(mark_safe(getattr(apps.get_app_config('Contactform'), name)))

@register.inclusion_tag('contactform/_recaptcha_field.html')
def recaptcha_field():
    """ Prints a recaptcha field using bootstrap4 """
    recaptcha_enabled = apps.get_app_config('Contactform').recaptcha_enabled
    recaptcha_sitekey = apps.get_app_config('Contactform').recaptcha_sitekey
    return{'recaptcha_enabled': recaptcha_enabled,
           'recaptcha_sitekey': recaptcha_sitekey}