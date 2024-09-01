from django.urls import path
from .views import ApiKeyView

urlpatterns = [
    path('', ApiKeyView.as_view(), name='api-keys'),
]
