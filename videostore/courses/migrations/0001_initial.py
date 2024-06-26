# Generated by Django 4.0.4 on 2024-05-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Имя курса на латинице')),
                ('title', models.CharField(max_length=120, verbose_name='Название курса')),
                ('desc', models.TextField(verbose_name='Описание курса')),
                ('image', models.ImageField(default='default.png', upload_to='course_images', verbose_name='Изображение курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
