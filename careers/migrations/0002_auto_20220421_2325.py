# Generated by Django 3.0.14 on 2022-04-21 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='job_name',
            new_name='career_name',
        ),
    ]
