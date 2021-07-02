from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class ContactformConfig(AppConfig):

    # Name for the application to be included in INSTALLED_APPS
    name = 'contactform'

    # Short name for the application, used to get attributes
    label = 'Contactform'                                        

    # App name for the Administration Site
    verbose_name  = "Django Contact-Form"

    # Application settings 
    pagination          = 5                                                 # Pagination elements
    meta_title          = "Django Contact-Form"                             # Meta Title
    header_title        = "Django<strong>ContactForm</strong>"              # Header Title
    header_description  = _("A reusable contact form developed for Django") # Header Description
    footer              = _("Proudly powered by PZ-Django-Contactform")     # Footer message

    # Recipients for the contact form
    contact_form_recipient = "you@yourdomain.com"

    # Recaptcha
    recaptcha_enabled   = True
    recaptcha_sitekey   = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI' 
    recaptcha_secret    = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'