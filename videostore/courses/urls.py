from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

# Список маршрутов (URL patterns) для приложения.
urlpatterns = [
    # Маршрут для главной страницы. Обрабатывается классом HomePage из views.
    # Использование cache_page(60 * 5) для кэширования страницы на 5 минут.
    path('', cache_page(60 *5)(views.HomePage.as_view()), name='home'),

    # Маршрут для страницы тарифов. Обрабатывается функцией tarrifsPage из views.
    path('tarrifs', views.tarrifsPage, name='tarrifs'),

    # Маршрут для детальной страницы курса. Обрабатывается классом CourseDetailPage из views.
    # Использует параметр <slug> для идентификации курса.
    # Использование cache_page(60 * 5) для кэширования страницы на 5 минут.
    path('course/<slug>', cache_page(60 * 5)(views.CourseDetailPage.as_view()), name='course-detail'),

    # Маршрут для детальной страницы урока. Обрабатывается классом LessonDetailPage из views.
    # Использует параметры <slug> для идентификации курса и <lesson_slug> для идентификации урока.
    # Использование cache_page(60 * 5) для кэширования страницы на 5 минут.
    path('course/<slug>/<lesson_slug>', cache_page(60 * 5)(views.LessonDetailPage.as_view()), name='lesson-detail'),
]
