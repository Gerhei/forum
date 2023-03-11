from django.core.exceptions import ObjectDoesNotExist

from src.forum.dto.topic import TopicDetailDto
from src.common.exceptions.domain_exceptions import EntityNotFound, AccessError
from src.forum.models import Topic, Comment


class TopicService:
    def get_topic(self, slug: str) -> TopicDetailDto:
        try:
            topic = Topic.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound('Topic not found.')
        return TopicDetailDto.create(topic)

    def create_topic(self, name: str, section_id: int, comment: str, user) -> Topic:
        try:
            topic = Topic.objects.create(name=name, section_id=section_id, user=user)
        except ObjectDoesNotExist:
            raise EntityNotFound('Section not found.')
        comment = Comment(text=comment, user=user, topic=topic)
        comment.save()
        return topic

    def create_comment(self, topic_id: int, text: str, user) -> Comment:
        try:
            topic = Topic.objects.get(id=topic_id)
        except ObjectDoesNotExist:
            raise EntityNotFound('Topic not found.')
        comment = Comment.objects.create(topic=topic, text=text, user=user)
        return comment

    @classmethod
    def get_comment(cls, comment_id: int) -> Comment:
        try:
            comment = Comment.objects.get(id=comment_id)
        except ObjectDoesNotExist:
            raise EntityNotFound('Comment not found.')
        return comment

    @classmethod
    def update_comment(cls, comment: Comment, text: str) -> Comment:
        if not comment.is_editable():
            raise AccessError('This comment can\'t be edited because time has passed during '
                              'which it could have been edited.')
        comment.text = text
        comment.save()
        return comment
