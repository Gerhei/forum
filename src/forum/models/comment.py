from datetime import datetime, timedelta

from django.db import models

COMMENT_IS_EDITABLE_SECONDS = 600


class Comment(models.Model):
    text = models.TextField(max_length=15000, verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updating time')
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True, verbose_name='author')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, verbose_name='topic')

    def __str__(self):
        return f'Comment №{self.pk}'

    def is_changed(self):
        return self.updated_at - self.created_at > timedelta(seconds=1)

    def is_editable(self):
        return datetime.now() - self.created_at < timedelta(seconds=COMMENT_IS_EDITABLE_SECONDS)

    def is_editable_for_user(self, account):
        """It is possible to edit only your own comments only for a certain time after creation"""
        return all([account, self.is_editable(), self.account == account])

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        ordering = ('topic', 'created_at')
