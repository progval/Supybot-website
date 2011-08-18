from news.models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_display = ('title', 'slug', 'author', 'created_at', 'updated_at', 'published')
    search_fields = ['title', 'body', 'author']
    ordering = ('-created_at',)

    fieldsets = [
        ('Metadata', {'fields': ['title', 'slug', 'author', 'published']}),
        ('Content', {'fields': ['short_description', 'body']}),
    ]

admin.site.register(News, NewsAdmin)
