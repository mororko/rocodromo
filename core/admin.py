from django.contrib import admin
from .models import Notice


# Register your models here.
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', "start_at", "end_at")
    list_filter = ('is_active',)
    search_fields = ('title', 'body')