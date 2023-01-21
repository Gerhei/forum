from django.core.exceptions import ObjectDoesNotExist

from src.common.exceptions.domain_exceptions import EntityNotFound
from src.forum.dto.section import SectionListDto
from src.forum.models import Section


class SectionService:
    def get_section(self, slug: str) -> Section:
        try:
            section = Section.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound
        return section

    def get_section_list(self, parent_slug: str | None) -> SectionListDto:
        if not parent_slug:
            sections = Section.objects.filter(parent=None)
            return SectionListDto(sections=sections)
        try:
            sections = Section.objects.get(slug=parent_slug).children
        except ObjectDoesNotExist:
            raise EntityNotFound
        return SectionListDto(sections=sections)
