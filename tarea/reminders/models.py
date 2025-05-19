import uuid
from django.db import models

class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=120, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-important', 'created_at']

    def __str__(self):
        return self.content
    