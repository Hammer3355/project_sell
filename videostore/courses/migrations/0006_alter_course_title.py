# Generated by Django 4.0.4 on 2024-05-23 05:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_is_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]