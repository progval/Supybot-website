from plugins.models import Plugin
from django.contrib import admin

class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
    search_fields = ['name', 'description', 'author']
    ordering = ('-created_at',)

    fieldsets = [
        ('Metadata', {'fields': ['name', 'author', 'published', 'minimal_version']}),
        ('Access', {'fields': ['git_repo', 'url']}),
        ('About', {'fields': ['short_description', 'description']}),
    ]

admin.site.register(Plugin, PluginAdmin)

