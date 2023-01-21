from dataclasses import dataclass


@dataclass
class SectionDto:
    id: int
    name: str
    slug: str


@dataclass
class SectionListDto:
    sections: list[SectionDto]
