# Generated by Django 5.0.4 on 2024-04-23 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профайл', 'verbose_name_plural': 'Профайлы'},
        ),
    ]