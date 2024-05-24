from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    # Маршрут для регистрации нового пользователя
    path('reg/', userViews.register, name='reg'),

    # Маршрут для просмотра профиля пользователя
    path('profile/', userViews.profile, name='profile'),

    # Маршрут для входа пользователя (аутентификации)
    path('', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),

    # Маршрут для сброса пароля пользователя
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass-reset'),

    # Маршрут для подтверждения сброса пароля
    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # Маршрут для завершения сброса пароля
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    # Маршрут для успешного сброса пароля
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    # Маршрут для выхода пользователя (разлогинивания)
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]

