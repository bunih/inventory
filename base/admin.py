from django.contrib import admin
from .models import Activity
# Register your models here.


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'weapon', 'site',
        'status',
        'start_time',
        'end_time',
    ]
