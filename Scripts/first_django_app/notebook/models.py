from django.db import models


class NotebookRow(models.Model):
    class Meta:
        db_table = 'notebook_rows'

    description = models.TextField()
    date = models.DateTimeField()
    position = models.IntegerField()
    status = models.IntegerField()
