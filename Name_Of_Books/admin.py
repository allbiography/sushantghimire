from django.contrib import admin
from .models import Novels


@admin.register(Novels)
class Text_BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
