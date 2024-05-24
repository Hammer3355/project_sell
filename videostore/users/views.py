from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistraion, ProfileImage, UserUpdateForm

def register(request):
    """
    Представление для регистрации нового пользователя.

    Если запрос методом POST, проверяет введенные данные формы.
    Если форма валидна, сохраняет пользователя и перенаправляет на страницу входа.
    Иначе отображает форму регистрации.

    Параметры:
    - request: HTTP-запрос.

    Возвращает:
    - Отображает страницу регистрации с формой.
    """
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('user')  # Перенаправление на страницу входа
    else:
        form = UserOurRegistraion()  # Создание новой формы регистрации
    return render(request, 'users/register.html', {'form': form, 'title': 'Регистрация пользователя'})

@login_required  # Декоратор, требующий аутентификации пользователя для доступа к представлению
def profile(request):
    """
    Представление для просмотра и обновления профиля пользователя.

    Если запрос методом POST, проверяет введенные данные форм профиля и пользователя.
    Если формы валидны, сохраняет обновленные данные профиля и пользователя.
    Иначе отображает формы для редактирования.

    Параметры:
    - request: HTTP-запрос.

    Возвращает:
    - Отображает страницу профиля с формами для редактирования.
    """
    if request.method == "POST":
        # Создание экземпляра формы для обновления изображения профиля с данными из запроса и файлами
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        # Создание экземпляра формы для обновления данных пользователя с данными из запроса
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')  # Перенаправление на страницу профиля
    else:
        # Создание экземпляра формы для обновления изображения профиля с данными профиля пользователя
        img_profile = ProfileImage(instance=request.user.profile)
        # Создание экземпляра формы для обновления данных пользователя с данными профиля пользователя
        update_user = UserUpdateForm(instance=request.user)

    # Подготовка данных для передачи в шаблон
    data = {
        'img_profile': img_profile,  # Форма для обновления изображения профиля
        'update_user': update_user   # Форма для обновления данных пользователя
    }

    return render(request, 'users/profile.html', data)  # Отображение страницы профиля с данными из data
