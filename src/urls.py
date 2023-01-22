from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from src.forum.views.comment.views import CommentView
from src.forum.views.topic.views import TopicView
from src.forum.views.section.views import SectionView, SectionListView

API_PREFIX = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path(f'{API_PREFIX}/section/<str:slug>', SectionView.as_view(), name='section'),
    path(f'{API_PREFIX}/section', SectionListView.as_view(), name='section-list'),
    path(f'{API_PREFIX}/topic/create', TopicView.as_view(), name='create-topic'),
    path(f'{API_PREFIX}/topic/<str:slug>', TopicView.as_view(), name='get-topic'),
    path(f'{API_PREFIX}/comment/create', CommentView.as_view(), name='create-comment'),
    path(f'{API_PREFIX}/comment/update', CommentView.as_view(), name='update-comment'),
]
