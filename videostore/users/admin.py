from django.contrib import admin
from .models import Profile

# Регистрация модели Profile в административной панели Django.
# Это позволит вам управлять объектами профиля через интерфейс администратора.
admin.site.register(Profile)
