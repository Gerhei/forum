import os

from django.contrib.auth import get_user_model
from django.db import models
from slugify import slugify


def avatar_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.username, ext)
    return os.path.join('forum/user_avatars', filename)


class Account(models.Model):
    slug = models.SlugField(unique=True, editable=False, verbose_name='URL')
    # avatar = models.ImageField(
    #     blank=True,
    #     upload_to=avatar_filename,
    #     # default='/forum/user_avatars/default_profile.jpg',
    #     verbose_name='profile avatar'
    # )
    description = models.TextField(blank=True, verbose_name='about yourself')
    reputation = models.IntegerField(default=0, verbose_name='reputation')
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Account, self).save(*args, **kwargs)

    @property
    def username(self):
        return self.user.username

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        ordering = ('user',)
