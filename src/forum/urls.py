from django.urls import path

from src.forum.views.comment.views import CommentCreateView, CommentUpdateView
from src.forum.views.section.views import SectionView, SectionListView
from src.forum.views.topic.views import TopicCreateView, TopicView

urlpatterns = [
    path('section/<str:slug>', SectionView.as_view(), name='section'),
    path('section', SectionListView.as_view(), name='section-list'),
    path('topic/create', TopicCreateView.as_view(), name='create-topic'),
    path('topic/get/<str:slug>', TopicView.as_view(), name='get-topic'),
    path('comment/create', CommentCreateView.as_view(), name='create-comment'),
    path('comment/update/<int:pk>', CommentUpdateView.as_view(), name='update-comment'),
]
