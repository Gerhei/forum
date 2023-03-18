from django.urls import path

from src.forum.views.comment.views import CommentCreateView
from src.forum.views.topic.views import TopicView, TopicCreateView
from src.forum.views.section.views import SectionView

urlpatterns = [
    path('', SectionView.as_view(), name="section"),
    path('topic/<slug:slug>', TopicView.as_view(), name="topic"),
    path('topic/create/<slug:section_slug>', TopicCreateView.as_view(), name="create_topic"),
    path('comment/create/<int:topic_pk>', CommentCreateView.as_view(), name="create_comment"),
]
