from django.http import Http404
from django.views.generic import TemplateView

from src.common.exceptions.domain_exceptions import EntityNotFound
from src.forum.dto.section import SectionDetailDto
from src.forum.services.section import SectionService


class SectionView(TemplateView):
    template_name = 'section.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self._get_section(slug=self.request.GET.get('section', None))
        context['section_list'] = section.children
        context['topic_list'] = section.topics
        return context

    def _get_section(self, slug: str | None) -> SectionDetailDto:
        try:
            section = SectionService().get_section(slug=slug)
        except EntityNotFound:
            raise Http404()
        return section
