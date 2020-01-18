from django.contrib import admin
from todo.models import Task, Profile


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(Profile, ProfileAdmin)
