from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todo_user'

    def __str__(self):
        return self.name


class Task(models.Model):
    user_profile = models.ForeignKey(Profile, null=False, on_delete=models.DO_NOTHING)
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
