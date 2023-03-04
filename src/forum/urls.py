from django.urls import path

from src.forum.views.section.views import SectionView

urlpatterns = [
    path('', SectionView.as_view(), name="section-list"),
    # path('topic/<slug:slug>', TopicDetailView.as_view(), name="topic"),
    # path('topic/create/<slug:section_slug>', TopicCreateView.as_view(), name="create_topic"),
    # path('comment/update/<int:pk>', CommentUpdateView.as_view(), name="update_post"),
    # path('comment/create/<int:pk>', CommentCreateView.as_view(), name="create_post"),
]
