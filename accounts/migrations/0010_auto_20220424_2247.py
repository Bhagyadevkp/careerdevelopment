# Generated by Django 3.2.13 on 2022-04-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_student_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='qualification',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.ImageField(null=True, upload_to='picture'),
        ),
    ]
