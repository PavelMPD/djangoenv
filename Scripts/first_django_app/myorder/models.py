from django.db import models

# Create your models here.
class MyOrder(models.Model):
    class Meta:
        db_table = 'myorder'

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()