from django.contrib import admin
from .models import students

class student(admin.ModelAdmin):
    list_display=('name', 'number', 'year', 'dept', 'section')
    list_filter = ('year', 'dept', 'section')
    search_fields = ['number', 'year', 'dept', 'section']

admin.site.register(students, student)

