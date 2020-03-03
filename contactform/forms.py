from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required = True, max_length=128)
    email = forms.EmailField(required = True)
    subject = forms.CharField(required = True)
    message = forms.CharField(widget=forms.Textarea, required = True)

    class Meta:
        fields = ('Full Name','E-mail address','Subject','Message')      