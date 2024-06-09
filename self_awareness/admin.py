from django.contrib import admin

# Register your models here.
from .models import Sleep

class SleepAdmin(admin.ModelAdmin):
    list_display=['date','sleep_time','get_up_time','last_modified_time','get_sleep_duration']

admin.site.register(Sleep,SleepAdmin)