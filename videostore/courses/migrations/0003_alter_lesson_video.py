# Generated by Django 4.2 on 2024-05-09 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.URLField(verbose_name='Ссылка на видео'),
        ),
    ]
