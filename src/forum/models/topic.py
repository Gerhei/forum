from django.contrib.auth import get_user_model
from django.db import models
from slugify import slugify


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name='title')
    slug = models.SlugField(max_length=100, unique=True, editable=False, verbose_name='URL')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='user')
    section = models.ForeignKey(
        'Section',
        on_delete=models.PROTECT,
        related_name='topics',
        verbose_name='section'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time')

    def __str__(self):
        return f'Topic "{self.name}"'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.section.name}-{self.name}')
        super(Topic, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"
        ordering = ('-created_at', 'name')
        unique_together = (('name', 'section'),)
