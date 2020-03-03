from django.urls import path, include
from . import views

# App name
app_name = 'contactform'

# Url Patterns
urlpatterns = [
    path('', views.form, name = 'contact'),
    path('success/', views.success, name = 'success'),
]
