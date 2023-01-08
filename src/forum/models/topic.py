from django.db import models
from django.utils.text import slugify


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name='title')
    slug = models.SlugField(max_length=100, unique=True, editable=False, verbose_name='URL')
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True, verbose_name='author')
    section = models.ForeignKey('Section', on_delete=models.PROTECT, verbose_name='section')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time')

    def __str__(self):
        return f'Topic "{self.name}"'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}-{self.account.user.username}')
        super(Topic, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"
        ordering = ('-created_at', 'name')
        unique_together = (('name', 'account'),)
