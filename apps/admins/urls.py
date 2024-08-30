from django.urls import path
from .views import (  
    ComponentAdminView,
    ComponentDetailAdminView,
    ComponentFileAdminView,
    ComponentFileDetailAdminView,
)

urlpatterns = [
    path('components/', ComponentAdminView.as_view(), name='admin-component-list'),
    path('components/<int:pk>/',ComponentDetailAdminView.as_view(),name='admin-component-detail',),
    path('files/', ComponentFileAdminView.as_view(), name='admin-file-list'),
    path('files/<int:pk>/',ComponentFileDetailAdminView.as_view(),name='admin-file-detail'),
]
