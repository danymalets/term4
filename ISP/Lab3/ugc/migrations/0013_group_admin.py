# Generated by Django 2.2.23 on 2021-05-26 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0012_auto_20210527_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='administered_group', to='ugc.User', verbose_name='Админ'),
        ),
    ]
