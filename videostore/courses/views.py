from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Lesson

def tarrifsPage(request):
    """
    Обработчик для страницы тарифов.

    Отображает шаблон 'courses/tarrifs.html' с переданным заголовком.
    
    Параметры:
    - request: HTTP запрос.
    
    Возвращает:
    - HTTP ответ с отрендеренным шаблоном.
    """
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифы'})

class HomePage(ListView):
    """
    Представление для главной страницы.

    Отображает список всех курсов в шаблоне 'courses/home.html'.
    """
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Добавляет дополнительные данные в контекст шаблона.

        Параметры:
        - object_list: Список объектов, переданных в шаблон.
        - kwargs: Дополнительные аргументы.

        Возвращает:
        - ctx: Обновленный контекст с добавленным заголовком страницы.
        """
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx

class CourseDetailPage(DetailView):
    """
    Представление для детальной страницы курса.

    Отображает подробную информацию о курсе и связанных уроках в шаблоне 'courses/course-detail.html'.
    """
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Добавляет дополнительные данные в контекст шаблона.

        Параметры:
        - object_list: Список объектов, переданных в шаблон.
        - kwargs: Дополнительные аргументы.

        Возвращает:
        - ctx: Обновленный контекст с добавленным заголовком и списком уроков.
        """
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx

class LessonDetailPage(DetailView):
    """
    Представление для детальной страницы урока.

    Отображает подробную информацию о конкретном уроке в шаблоне 'courses/lesson-detail.html'.
    """
    model = Course
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Добавляет дополнительные данные в контекст шаблона.

        Параметры:
        - object_list: Список объектов, переданных в шаблон.
        - kwargs: Дополнительные аргументы.

        Возвращает:
        - ctx: Обновленный контекст с добавленным заголовком и информацией об уроке.
        """
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        # Uncomment this line if you need to process the video link.
        # lesson.video = lesson.video.split("v=")[1]

        ctx['title'] = lesson
        ctx['lesson'] = lesson
        return ctx
