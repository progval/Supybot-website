from get.models import DownloadLink
from django.contrib import admin

class DownloadLinkAdmin(admin.ModelAdmin):
    list_display = ('project', 'version', 'type')
    ordering = ('project', 'version', 'type')
    filter = ordering

    fieldsets = [
        ('Release data', {'fields': ['project', 'version', 'release_notes']}),
        ('Link', {'fields': ['type', 'link']}),
    ]

admin.site.register(DownloadLink, DownloadLinkAdmin)

