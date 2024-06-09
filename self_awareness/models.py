from django.db import models
from django.contrib import admin
from datetime import datetime,timedelta

# Create your models here.
class Sleep(models.Model):
    date=models.DateField()
    sleep_time=models.TimeField()
    get_up_time=models.TimeField()
    created_time=models.DateTimeField(auto_now_add=True)
    last_modified_time=models.DateTimeField(auto_now=True)

    @admin.display()
    def get_sleep_duration(self):
        sleep_datetime=datetime.combine(self.date,self.sleep_time)
        get_up_datetime=datetime.combine(self.date,self.get_up_time)
        sleep_duration=get_up_datetime-sleep_datetime

        if sleep_duration<timedelta(0):
            sleep_duration+=timedelta(days=1)
        return sleep_duration

    def __str__(self):
        return str(self.date)