from django.urls import path
from .views import ApiKeyView, ApiKeyInfoView

urlpatterns = [
    path("", ApiKeyView.as_view(), name="api-keys"),
    path("info/", ApiKeyInfoView.as_view(), name="api-keys-info"),
]
