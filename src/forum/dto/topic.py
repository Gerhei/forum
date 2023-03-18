from dataclasses import dataclass
from datetime import datetime

from src.forum.dto.comment import CommentDto
from src.forum.models import Topic


@dataclass
class TopicDto:
    id: int
    name: str
    slug: str
    user: str | None
    section: str
    created_at: datetime

    @classmethod
    def create(cls, topic: Topic) -> 'TopicDto':
        username = topic.user.username if topic.user else None
        return TopicDto(id=topic.id,
                        name=topic.name,
                        slug=topic.slug,
                        user=username,
                        section=topic.section.name,
                        created_at=topic.created_at)


@dataclass
class TopicDetailDto:
    id: int
    name: str
    slug: str
    user: str | None
    section: str
    created_at: datetime
    comments: list[CommentDto]

    @classmethod
    def create(cls, topic: Topic) -> 'TopicDetailDto':
        username = topic.user.username if topic.user else None
        comments = [CommentDto.create(comment) for comment in topic.get_comments()]
        return TopicDetailDto(id=topic.id,
                              name=topic.name,
                              slug=topic.slug,
                              user=username,
                              section=topic.section.name,
                              created_at=topic.created_at,
                              comments=comments)
