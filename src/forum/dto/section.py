from dataclasses import dataclass, field

from src.forum.dto.topic import TopicDto
from src.forum.models import Section

FAKE_ROOT_SECTION_ID = -1


@dataclass
class SectionDto:
    id: int
    name: str
    slug: str

    @classmethod
    def create(cls, section: Section) -> 'SectionDto':
        return SectionDto(id=section.id,
                          name=section.name,
                          slug=section.slug)


@dataclass
class SectionDetailDto:
    id: int
    name: str
    slug: str
    children: list[SectionDto] = field(default_factory=list)
    topics: list[TopicDto] = field(default_factory=list)
    parent: SectionDto | None = None

    @classmethod
    def create(cls, section: Section) -> 'SectionDetailDto':
        children = [SectionDto.create(child) for child in section.get_children()]
        topics = [TopicDto.create(topic) for topic in section.get_topics()]
        parent = SectionDto.create(section.parent) if section.parent else None
        return SectionDetailDto(id=section.id,
                                name=section.name,
                                slug=section.slug,
                                parent=parent,
                                children=children,
                                topics=topics)

    @classmethod
    def create_root_section(cls, children: list[Section]) -> 'SectionDetailDto':
        children = [SectionDto.create(child) for child in children]
        return SectionDetailDto(id=FAKE_ROOT_SECTION_ID,
                                name='',
                                slug='',
                                children=children)


@dataclass
class SectionListDto:
    sections: list[SectionDto]
