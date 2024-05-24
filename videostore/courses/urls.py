from django.urls import path
from . import views

# Список маршрутов (URL patterns) для приложения.
urlpatterns = [
    # Маршрут для главной страницы. Обрабатывается классом HomePage из views.
    path('', views.HomePage.as_view(), name='home'),

    # Маршрут для страницы тарифов. Обрабатывается функцией tarrifsPage из views.
    path('tarrifs', views.tarrifsPage, name='tarrifs'),

    # Маршрут для детальной страницы курса. Обрабатывается классом CourseDetailPage из views.
    # Использует параметр <slug> для идентификации курса.
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course-detail'),

    # Маршрут для детальной страницы урока. Обрабатывается классом LessonDetailPage из views.
    # Использует параметры <slug> для идентификации курса и <lesson_slug> для идентификации урока.
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail'),
]
