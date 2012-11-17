from django.db import models

from root.models import Fork

class DownloadLink(models.Model):
    project = models.ForeignKey(Fork, help_text='The fork to which belongs '
            'this download link.')
    version = models.CharField(max_length=512, help_text='A unique identifier '
            'of the version of this release.')

    release_notes = models.TextField(help_text='Other informations about that '
            'release.', blank=True)
    type = models.CharField(max_length=3, choices=(
        ('deb', 'Debian package'),
        ('rpm', 'Fedora package'),
        ('pkg', 'Other distribution package'),
        ('git', 'Git repository'),
        ('web', 'Web git or GitHub/Gitorious page.'),
        ('ftp', 'FTP repository'),
        ('tar', 'Tarball (compressed or not)'),
        ('zip', 'Zipball'),
        ('oth', 'Other'),
        ), help_text='The type of content this link points to.')

    link = models.CharField(max_length=4096)

