from django.core.exceptions import ObjectDoesNotExist

from src.common.exceptions.domain_exceptions import EntityNotFound
from src.forum.dto.section import SectionListDto, SectionDetailDto
from src.forum.models import Section


class SectionService:
    def get_section(self, slug: str | None) -> SectionDetailDto:
        if slug is None:
            root_sections = Section.objects.filter(parent=None)
            return SectionDetailDto.create_root_section(children=root_sections)

        try:
            section = Section.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound
        return SectionDetailDto.create(section)

    def get_section_list(self, parent_slug: str | None) -> SectionListDto:
        if not parent_slug:
            sections = Section.objects.filter(parent=None)
            return SectionListDto(sections=sections)
        try:
            sections = Section.objects.get(slug=parent_slug).children
        except ObjectDoesNotExist:
            raise EntityNotFound
        return SectionListDto(sections=sections)
