from django.db import models
from django.utils.text import slugify


class Section(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=100, unique=True, editable=False, verbose_name='URL')
    order = models.SmallIntegerField(default=0, editable=False, verbose_name='order')
    parent = models.ForeignKey(
        'Section',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='parent section'
    )

    def __str__(self):
        return f'Section "{self.name}"'

    def save(self, *args, **kwargs):
        if self.parent:
            self.order = self.parent.order + 1
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "section"
        verbose_name_plural = "sections"
        ordering = ('order', 'name')
