from django.db import models
from django.contrib.auth.models import User
from PIL import Image

TYPE_ACCOUNT = (
    ('full', 'Полный пакет'),
    ('free', 'Бесплатный пакет')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField - ОДИН К ОДНОМУ
    # Заменить картинку по умолчанию. После удалить этот коментарий
    img = models.ImageField('Фото пользователя', upload_to='user_images', default='default.png')
    account_type = models.CharField(verbose_name='Тип аккаунта', choices=TYPE_ACCOUNT, max_length=30, default='free')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width >256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)
    
    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'