from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label = _('Name'), required = True, max_length=128)
    email = forms.EmailField(label = _('E-Mail'), required = True)
    subject = forms.CharField(label = _('Subject'), required = True)
    message = forms.CharField(label = _('Message'), widget=forms.Textarea, required = True)

    class Meta:
        fields = ('Full Name','E-mail address','Subject','Message')      