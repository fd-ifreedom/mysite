from django.db import models

# Create your models here.
class Transaction(models.Model):
    date=models.DateField()
    from_whom=models.CharField(max_length=50)
    to_whom=models.CharField(max_length=50)
    amount=models.FloatField()
    description=models.CharField(max_length=100)
    created_time=models.DateTimeField(auto_now_add=True)
    last_modified_time=models.DateTimeField(auto_now=True)