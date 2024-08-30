from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('admins/', include('apps.admins.urls')),
    path('api-keys/', include('apps.keys.urls')),
    path('components/', include('apps.components.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
