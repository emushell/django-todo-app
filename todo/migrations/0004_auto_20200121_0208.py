# Generated by Django 2.2.9 on 2020-01-21 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200118_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]