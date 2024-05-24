from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserOurRegistraion(UserCreationForm):
    """
    Форма регистрации пользователей с дополнительным полем электронной почты.

    Параметры:
    - username: Имя пользователя.
    - password1: Пароль.
    - password2: Подтверждение пароля.
    - email: Электронная почта.
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления информации о пользователе.

    Параметры:
    - username: Имя пользователя.
    - email: Электронная почта.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImage(forms.ModelForm):
    """
    Форма обновления изображения профиля.

    Параметры:
    - img: Изображение профиля.
    """

    def __init__(self, *args, **kwards):
        """
        Конструктор класса ProfileImage.

        Изменяет метку поля img на "Изображение профиля".

        Параметры:
        - args: Позиционные аргументы.
        - kwards: Именованные аргументы.
        """
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']
