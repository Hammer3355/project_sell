from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Определение выбора типов аккаунтов
TYPE_ACCOUNT = (
    ('full', 'Полный пакет'),
    ('free', 'Бесплатный пакет')
)

class Profile(models.Model):
    """
    Модель профиля пользователя.

    Связывается с моделью пользователя Django через OneToOneField.
    Содержит информацию о пользователе, его изображении и типе аккаунта.

    Атрибуты:
    - user: Связь Один-к-Одному с моделью пользователя Django.
    - img: Изображение профиля пользователя.
    - account_type: Тип аккаунта пользователя (полный пакет или бесплатный пакет).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', upload_to='user_images', default='default.png')
    account_type = models.CharField(verbose_name='Тип аккаунта', choices=TYPE_ACCOUNT, max_length=30, default='free')

    def __str__(self):
        """
        Возвращает строковое представление объекта профиля.

        Возвращает:
        - Строка, содержащая имя пользователя.
        """
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        """
        Переопределенный метод сохранения объекта.

        При сохранении изображения профиля, проверяет его размер.
        Если размер больше 256x256 пикселей, изображение уменьшается до этого размера.

        Параметры:
        - args: Позиционные аргументы.
        - kwargs: Именованные аргументы.
        """
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width >256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        """
        Дополнительные настройки модели.

        verbose_name: Человекочитаемое имя модели в единственном числе.
        verbose_name_plural: Человекочитаемое имя модели во множественном числе.
        """
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
