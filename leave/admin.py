from django.contrib import admin
from .models import leave

class applications(admin.ModelAdmin):
    list_display=('title', 'number', 'year', 'dept', 'section')
    list_filter = ('year', 'dept', 'section')
    search_fields = ['number', 'year', 'dept', 'section']

admin.site.register(leave, applications)
