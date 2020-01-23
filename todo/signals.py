from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

DEFAULT_USER_GROUPS = ['default_user', 'delete_task', 'update_task', 'create_task']


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created')
        groups = Group.objects.filter(name__in=DEFAULT_USER_GROUPS)
        instance.groups.add(*groups)
        Profile.objects.create(user=instance, email=instance.email)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        # instance.profile.save()
        print('Profile updated!')
