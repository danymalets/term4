# Generated by Django 2.2.23 on 2021-05-26 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0019_remove_queue_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='display_name',
        ),
    ]