# Generated by Django 2.2.23 on 2021-05-25 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0004_auto_20210525_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ugc.Group', verbose_name='Группа'),
        ),
    ]
