# Generated by Django 2.2.23 on 2021-05-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0015_queue_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='users',
            field=models.ManyToManyField(blank=True, to='ugc.User', verbose_name='Участники очереди'),
        ),
    ]
