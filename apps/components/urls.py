from django.urls import path
from .views import (
    ComponentView,
    ComponentDetailView,
    ComponentFileView,
    ComponentFileDetailView,
)

urlpatterns = [
    path('', ComponentView.as_view(), name='component-list'),
    path('<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('files/', ComponentFileView.as_view(), name='file-list'),
    path('files/<int:pk>/', ComponentFileDetailView.as_view(), name='file-detail'),
]
