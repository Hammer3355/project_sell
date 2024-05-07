from django.db import models


class Course(models.Model):
    slug = models.SlugField('Имя курса на латинице')
    title = models.CharField('Название курса', max_length=120)
    desc = models.TextField('Описание курса')
    image = models.ImageField('Изображение курса', default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
