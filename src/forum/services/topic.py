from django.core.exceptions import ObjectDoesNotExist

from src.common.exceptions.domain_exceptions import EntityNotFound
from src.forum.models import Topic, Comment


class TopicService:
    def get_topic(self, slug: str) -> Topic:
        try:
            topic = Topic.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound
        return topic

    def create_topic(self, name: str, section_id: int, comment: str, user) -> Topic:
        topic = Topic.objects.create(name=name, section_id=section_id, user=user)
        comment = Comment(text=comment, user=user, topic=topic)
        comment.save()
        return topic
