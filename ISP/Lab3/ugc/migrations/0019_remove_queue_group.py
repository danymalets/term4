# Generated by Django 2.2.23 on 2021-05-26 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0018_remove_queue_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='group',
        ),
    ]
