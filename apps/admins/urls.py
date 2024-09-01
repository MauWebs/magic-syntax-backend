from django.urls import path
from .views import (  
    ComponentAdminView,
    ComponentDetailAdminView,
    ComponentFileAdminView,
    ComponentFileDetailAdminView,
)

urlpatterns = [
    path('components/', ComponentAdminView.as_view()),
    path('components/<int:pk>/', ComponentDetailAdminView.as_view()),
    path('components/<int:component_pk>/files/', ComponentFileAdminView.as_view()),
    path('components/<int:component_pk>/files/<int:pk>/', ComponentFileDetailAdminView.as_view()),
]
