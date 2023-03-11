from django.http import Http404
from django.views.generic import TemplateView

from src.common.exceptions.domain_exceptions import EntityNotFound
from src.forum.services.topic import TopicService


class TopicView(TemplateView):
    template_name = 'topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self._get_topic(slug=self.kwargs['slug'])
        context['topic'] = topic
        return context

    def _get_topic(self, slug: str):
        try:
            topic = TopicService().get_topic(slug=slug)
        except EntityNotFound:
            raise Http404()
        return topic
