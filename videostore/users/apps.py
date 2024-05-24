from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Конфигурация приложения Django для приложения 'users'.
    """

    name = 'users'  # Указываем имя приложения.

    def ready(self):
        """
        Метод ready вызывается, когда приложение Django готово к запуску.

        В данном случае, мы импортируем модуль users.signals. 
        Это позволяет автоматически загружать сигналы (слушатели событий) при запуске приложения.
        """
        import users.signals
