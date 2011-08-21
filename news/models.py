from django.contrib.auth.models import User
from django.db import models

class News (models.Model):
    author = models.ForeignKey(User, help_text='The user who wrote the news.')

    slug = models.SlugField(max_length=255, unique=True,
            help_text='A unique identifier used in the URL.')
    title = models.CharField(max_length=1024,
            help_text='The title of the news, as shown to the user.')
    short_description = models.TextField(max_length=4096,
            help_text='The content shown in the news list, after the title. '
            'Supports markdown formatting.')
    body = models.TextField(help_text='The content of the news. Supports '
            'markdown formatting.')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False,
            help_text='Whether or not the news is displayed to regular users.')

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return '/news/read/%s/' % self.slug

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-created_at']

class NewsComment(models.Model):
    key = models.ForeignKey(News)
    user = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
