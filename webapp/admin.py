from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'due_date', 'created_at']
    list_filter = ['status']
    search_fields = ['description', 'detailed_description']
    fields = ['description', 'detailed_description', 'status', 'due_date']