# Generated by Django 4.0.4 on 2024-05-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='Бесплатный курс?'),
        ),
    ]
