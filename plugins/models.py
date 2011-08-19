from django.contrib.auth.models import User
from django.db import models

from root.models import Fork

class Plugin(models.Model):
    author = models.ForeignKey(User, help_text='The user who wrote the plugin.')

    name = models.SlugField(max_length=512, help_text='The name of the plugin.')
    short_description = models.TextField(max_length=512, help_text='A short '
            'description of the plugin, shown in list view.')
    description = models.TextField(help_text='A full description of the '
            'plugin.')

    minimal_version = models.CharField(max_length=4096, help_text='The oldest '
            'Supybot version compatible with this plugin.', default='0.83.4.1')

    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    url = models.URLField(blank=True, help_text='The URL to the website for the plugin.')
    git_repo = models.CharField(max_length=512, help_text='The URL to the '
            'Git repository.')

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return '/plugins/view/%s/' % self.name

    class Meta:
        ordering = ['-created_at']
