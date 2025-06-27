from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='new')
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.description
