from django.urls import path
from .views import CheckEmailView, CheckEmailValidationView
urlpatterns = [
    path('linked/', CheckEmailView.as_view(), name='email'),
    path('validate/', CheckEmailValidationView.as_view(), name='validate')
]
