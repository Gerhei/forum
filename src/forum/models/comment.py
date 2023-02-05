from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

COMMENT_IS_EDITABLE_SECONDS = 600


class Comment(models.Model):
    text = models.TextField(max_length=15000, verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updating time')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='user')
    topic = models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='topic'
    )

    def __str__(self):
        return f'Comment №{self.pk}'

    def is_changed(self):
        return self.updated_at - self.created_at > timedelta(seconds=1)

    def is_editable(self):
        """It is possible to edit only for a certain time after creation"""
        is_new_comment = timezone.now() - self.created_at < timedelta(seconds=COMMENT_IS_EDITABLE_SECONDS)
        return is_new_comment

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        ordering = ('topic', 'created_at')
