from django.contrib import admin
from .models import notify
from django_summernote.admin import SummernoteModelAdmin


class updatesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'time')
    list_filter = ('year', 'dept', 'section')
    search_fields = [ 'year', 'dept', 'section']
    summernote_fields = ('content',)

#admin.site.register(notify)
admin.site.register(notify)
