from django.core.exceptions import ObjectDoesNotExist

from src.common.exceptions.domain_exceptions import EntityNotFound, AccessError
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

    def create_comment(self, topic_id: int, text: str, user) -> Comment:
        try:
            topic = Topic.objects.get(id=topic_id)
        except ObjectDoesNotExist:
            raise EntityNotFound
        comment = Comment.objects.create(topic=topic, text=text, user=user)
        return comment

    def update_comment(self, comment_id: int, text: str, user) -> Comment:
        try:
            comment = Comment.objects.get(id=comment_id)
        except ObjectDoesNotExist:
            raise EntityNotFound
        if not comment.is_editable(user=user):
            raise AccessError('This comment can\'t be edited because you are not author or the time has passed during '
                              'which it could have been edited.')
        comment.text = text
        comment.save()
        return comment
