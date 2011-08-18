from plugins.models import Plugin
from django.contrib import admin

class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
    search_fields = ['name', 'description', 'author']
    ordering = ('-created_at',)

    fieldsets = [
        ('About', {'fields': ['name', 'author', 'published', 'url', 'short_description', 'description']}),
        ('Access', {'fields': ['git_repo', 'works_with']}),
    ]

admin.site.register(Plugin, PluginAdmin)

