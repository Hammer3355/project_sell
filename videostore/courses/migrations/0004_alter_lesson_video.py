# Generated by Django 4.0.4 on 2024-05-10 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(max_length=200, verbose_name='Ссылка на видео'),
        ),
    ]