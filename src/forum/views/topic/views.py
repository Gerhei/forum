from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView, FormView

from src.forum.forms.comment import CommentForm
from src.forum.services.section import SectionService
from src.forum.forms.topic import TopicForm
from src.common.exceptions.domain_exceptions import EntityNotFound
from src.forum.services.topic import TopicService


class TopicView(TemplateView):
    template_name = 'topic.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self._get_topic(slug=self.kwargs['slug'])
        context['topic'] = topic
        context['form'] = CommentForm()
        return context

    def _get_topic(self, slug: str):
        try:
            topic = TopicService().get_topic(slug=slug)
        except EntityNotFound:
            raise Http404()
        return topic


class TopicCreateView(LoginRequiredMixin, FormView):
    template_name = 'create_topic.html'
    form_class = TopicForm

    def setup(self, request, *args, **kwargs):
        self.section = self._get_section(slug=kwargs['section_slug'])
        super(TopicCreateView, self).setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = self.section
        return context

    def form_valid(self, form):
        topic = TopicService().create_topic(name=form.cleaned_data['name'],
                                            section_id=self.section.id,
                                            comment=form.cleaned_data['text'],
                                            user=self.request.user)
        return HttpResponseRedirect(topic.get_absolute_url())

    def _get_section(self, slug: str):
        try:
            section = SectionService().get_section(slug=slug)
        except EntityNotFound:
            raise Http404()
        return section
