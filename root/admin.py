from root.models import Fork
from django.contrib import admin

class ForkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

    fieldsets = [
        ('Main informations', {'fields': ['name', 'maintainer', 'website']}),
        ('Other informations', {'fields': ['based_on', 'description']}),
    ]

admin.site.register(Fork, ForkAdmin)


