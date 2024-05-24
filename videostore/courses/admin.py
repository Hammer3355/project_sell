# Импортируем модуль админки из Django
from django.contrib import admin

# Импортируем модели Course и Lesson из текущего приложения
from .models import Course, Lesson

# Регистрируем модель Course в административной панели
admin.site.register(Course)

# Регистрируем модель Lesson в административной панели
admin.site.register(Lesson)



