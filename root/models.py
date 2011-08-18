from django.contrib.auth.models import User
from django.db import models

class Fork(models.Model):
    maintainer = models.ForeignKey(User, help_text='The user who own this '
            'fork.', blank=True, null=True)
    name = models.CharField(max_length=128)

    description = models.TextField(help_text='What does this project aim to '
            'do?')

    based_on = models.ManyToManyField('self', blank=True, null=True)

    website = models.URLField()

    def __unicode__(self):
        return self.name
