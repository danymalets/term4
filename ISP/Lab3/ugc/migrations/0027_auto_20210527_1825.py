# Generated by Django 2.2.23 on 2021-05-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0026_queue_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='creator',
        ),
        migrations.AlterField(
            model_name='queue',
            name='name',
            field=models.DateTimeField(null=True, verbose_name='Дата события'),
        ),
    ]
