# Generated by Django 3.2.13 on 2022-04-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220424_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(null=True, upload_to='pictures'),
        ),
    ]
