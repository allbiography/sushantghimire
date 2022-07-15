from django.contrib import admin
from .models import history


@admin.register(history)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'book',
                    'issued_date',
                    'due_date',
                    'returned_date')
    ordering = ('student',)
    search_fields = ['student']
