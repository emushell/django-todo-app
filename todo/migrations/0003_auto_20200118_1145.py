# Generated by Django 2.2.9 on 2020-01-18 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200118_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='todo.Profile'),
        ),
    ]