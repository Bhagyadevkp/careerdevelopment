# Generated by Django 3.2.13 on 2022-04-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AddField(
            model_name='student',
            name='resume',
            field=models.FileField(null=True, upload_to='resume', verbose_name='resume'),
        ),
    ]