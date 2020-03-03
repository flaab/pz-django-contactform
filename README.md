# Yet another Django Contact Form

A bootstrapped, captha protected and customizable django contact form app for your django website. 

![PZ-Django-Contactform](https://www.dropbox.com/s/fzvl4jp0vb7i8bo/djangocontact.png?raw=1)

## Requirements
- Python >= 3.0
- Django >= 2.2.6
- Crispy-forms
- Hashlib

## Installation
Create a directory and clone the project.
```
$ mkdir mysite
$ cd mysite
$ git clone https://github.com/flaab/pz-django-contactform.git 
```
Create the database and tables of the application.
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
Create a superuser for django-admin.
```
$ python3 manage.py createsuperuser
```
If all went well, run the server.
```
$ python3 manage.py runserver
```
Now the server is up and running and the app is available at http://127.0.0.1:8000 and http://127.0.0.1:8000/contact.

## Running the application in a existing Django Site

The above instructions will create a new Django project that will run the application. If you did that, you can skip this section. If on the other hand, you want to include the accounts application in your existing project, then another course of action is needed. Add the following lines in your *settings.py*:

```
# Imports
from django.contrib.messages import constants as messages

# Installed apps
INSTALLED_APPS = (
    # ...
    'django.contrib.staticfiles',
    'crispy_forms',
    'contactform',
)

# Crispy template pack
CRISPY_TEMPLATE_PACK = 'bootstrap4

# Static files and media
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Email backend 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = ‘smtp.server.com’
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ‘your_account@server.com’
EMAIL_HOST_PASSWORD = ‘’

# Bootstrap messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
```

Add the following lines in your *urls.py*:

```
urlpatterns = [
    # ...,
    path('contact/', include(('contactform.urls', 'contact'), namespace = 'contact')),
]
if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
```

## Customize the application
To further customize the application to do what you need, you can:

- Configure the application constants at *contactform/apps.py*
- Edit the **ContactForm** at *contactform/forms.py*, adding or removing user profile fields.
- Add or edit views at *account/views.py*, adding or customizing functionality
- Customize the templates at *contactform/templates* to look they way you want.

## Customize the templates
The templates are organized in three categories: extendable templates, includable templates and page templates. Each uses a different naming convention. The templates the application uses are the following, which you can edit to fit your needs. Stylesheets and Javascript files are hotlinked from cdn repositories but you can place your own under *account/static/*.

- *templates/_messages.html* => Template to display flash messages (error, warning, validation error, success)
- *templates/contactform/__l_base.html* => Base layout for the application 
- *templates/contactform/_sidebar.html* => Navigation sidebar template
- *templates/contactform/_recaptcha_field.html => Template for the recaptcha field inclusion tag 
- *templates/contactform/form.html* => Template for the contact form page
- *templates/contactform/success.html* => Template for the success page

## Authors
**Arturo Lopez Perez** - Main and sole developer (so far).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
