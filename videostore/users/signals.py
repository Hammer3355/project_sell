from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# Сигнал, который создает профиль пользователя при создании нового пользователя
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Создание профиля пользователя при создании нового пользователя.

    Параметры:
    - sender: Класс модели, отправивший сигнал.
    - instance: Созданный экземпляр объекта (пользователь).
    - created: Флаг, указывающий на создание объекта.
    - kwargs: Дополнительные аргументы.
    """
    if created:
        Profile.objects.create(user=instance)

# Сигнал, который сохраняет профиль пользователя при обновлении данных пользователя
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Сохранение профиля пользователя при обновлении данных пользователя.

    Параметры:
    - sender: Класс модели, отправивший сигнал.
    - instance: Экземпляр объекта (пользователь).
    - kwargs: Дополнительные аргументы.
    """
    instance.profile.save()
