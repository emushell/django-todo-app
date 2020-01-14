from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'tasks'

    @classmethod
    def create(cls, title):
        task = cls(title=title)
        return task

    def __str__(self):
        return self.title
