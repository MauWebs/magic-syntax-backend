from django.urls import path
from .views import ApiKeyView, ApiKeyTestView

urlpatterns = [
    path('', ApiKeyView.as_view(), name='api-keys'),
    path('test/', ApiKeyTestView.as_view(), name='api-keys-test'),
]
