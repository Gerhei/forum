from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

API_PREFIX = 'api'

urlpatterns = [
    path('', include('src.forum.urls')),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path(f'{API_PREFIX}/', include('src.forum.api_urls')),
    path(f'{API_PREFIX}/auth/', include('src.users.urls')),
]
