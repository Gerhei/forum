from django.db import models
from slugify import slugify


class Section(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=100, unique=True, editable=False, verbose_name='URL')
    order = models.SmallIntegerField(default=0, editable=False, verbose_name='order')
    parent = models.ForeignKey(
        'Section',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='parent section'
    )

    def __str__(self):
        return f'Section "{self.name}"'

    def save(self, *args, **kwargs):
        if self.parent:
            self.order = self.parent.order + 1
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)

    def get_children(self) -> list['Section']:
        return self.children.all()

    def get_topics(self) -> list:
        return self.topics.all()

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ('order', 'name')
