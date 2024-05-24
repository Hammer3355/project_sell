from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Course(models.Model):
    """
    Модель для представления курса.
    
    Атрибуты:
    - slug: Короткое имя курса на латинице для URL.
    - title: Название курса.
    - desc: Описание курса с возможностью загрузки медиафайлов.
    - image: Изображение курса, загружаемое в папку 'course_images', по умолчанию 'default.png'.
    - is_free: Флаг, указывающий, бесплатный курс или нет.
    """
    
    slug = models.SlugField('Имя курса на латинице')
    title = models.CharField('Название курса', max_length=120)
    desc = RichTextUploadingField('Описание')
    image = models.ImageField('Изображение курса', default='default.png', upload_to='course_images')
    is_free = models.BooleanField('Бесплатный курс?', default=True)

    def __str__(self):
        """
        Возвращает строковое представление модели.
        В данном случае, это название курса.
        """
        return self.title

    class Meta:
        """
        Дополнительные настройки модели.
        
        verbose_name: Человекочитаемое имя модели в единственном числе.
        verbose_name_plural: Человекочитаемое имя модели во множественном числе.
        """
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для доступа к детальной информации о курсе.
        
        Использует именованный маршрут 'course-detail' и передает параметр 'slug'.
        """
        return reverse('course-detail', kwargs={'slug': self.slug})

class Lesson(models.Model):
    """
    Модель для представления урока.
    
    Атрибуты:
    - slug: Короткое имя урока на латинице для URL.
    - title: Название урока.
    - desc: Описание урока с возможностью загрузки медиафайлов.
    - course: Ссылка на связанный курс (внешний ключ).
    - number: Номер урока в курсе.
    - video: Ссылка на видео урока.
    """
    
    slug = models.SlugField('Имя урока на латинице')
    title = models.CharField('Название урока', max_length=120)
    desc = RichTextUploadingField('Описание')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс?')
    number = models.IntegerField('Номер урока')
    video = models.CharField('Ссылка на видео', max_length=200)

    def __str__(self):
        """
        Возвращает строковое представление модели.
        В данном случае, это название урока.
        """
        return self.title

    class Meta:
        """
        Дополнительные настройки модели.
        
        verbose_name: Человекочитаемое имя модели в единственном числе.
        verbose_name_plural: Человекочитаемое имя модели во множественном числе.
        """
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для доступа к детальной информации о уроке.
        
        Использует именованный маршрут 'lesson-detail' и передает параметры 'slug' курса и 'lesson_slug' урока.
        """
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})
