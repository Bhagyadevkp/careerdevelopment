# Generated by Django 3.2.13 on 2022-04-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0002_auto_20220422_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='qualification',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
