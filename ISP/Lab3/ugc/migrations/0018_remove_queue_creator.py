# Generated by Django 2.2.23 on 2021-05-26 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0017_remove_queue_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='creator',
        ),
    ]
