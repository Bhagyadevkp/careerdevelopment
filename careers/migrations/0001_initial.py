# Generated by Django 3.2.13 on 2022-04-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='picture')),
                ('img1', models.ImageField(null=True, upload_to='picture')),
                ('img2', models.ImageField(null=True, upload_to='picture')),
                ('img3', models.ImageField(null=True, upload_to='picture')),
                ('description', models.TextField()),
                ('video', models.FileField(null=True, upload_to='video', verbose_name='video')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('vacancy', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]
