from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at', 'clicks_count')

admin.site.register(Link, LinkAdmin)


