from django.urls import path
from .views import (
    ComponentView,
    ComponentDetailView,
    ComponentFileView,
    ComponentFileDetailView,
)

urlpatterns = [
    path('', ComponentView.as_view()),
    path('<int:pk>/', ComponentDetailView.as_view()),
    path('<int:component_id>/files/', ComponentFileView.as_view()),
    path('<int:component_id>/files/<int:pk>/', ComponentFileDetailView.as_view()),
]
