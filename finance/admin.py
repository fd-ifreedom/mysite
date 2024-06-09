from django.contrib import admin
from .models import Transaction
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display=['date','from_whom','to_whom','amount','description','last_modified_time']
#    list_filter=['date','from_whom','to_whom']

admin.site.register(Transaction,TransactionAdmin)