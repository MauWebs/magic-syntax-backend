from django.urls import path

from .views import AuthDeviceView


urlpatterns = [
    path('', AuthDeviceView.as_view()),
]
