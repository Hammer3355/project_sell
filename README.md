# Дипломный проект

Пара слов о проекте.

### Суть проекта, сайт обучения менеджеров маркетплейсов,способ обучения - видео-формат

[Сам  сайт](https://sellmen.ru/)

[Хостинг](https://hosting.timeweb.ru/)

[Мануал по деплою сайта](https://timeweb.com/ru/docs/virtualnyj-hosting/prilozheniya-i-frejmvorki/django/)


#### Установка проекта на свой IDE

1. Клонировть проект командой
``` python
git clone https://github.com/Hammer3355/project_sell.git
```
2. Создание виртуального окружения
``` python
python -m venv venv
```
3. Активация
``` python
venv\Scripts\activate
```
4. Установка зависимостей из файла pip install -r requirements.txt
``` python
pip install -r requirements.txt
```
В данном проекте все пароли и ключи доступа спрятаны в файл .env
так что вам придется записать в него свои данные. Выглядит это примерно так:
``` python
SOCIAL_AUTH_GITHUB_KEY = 'ВАШИ ЗНАЧЕНИЯ'
SOCIAL_AUTH_GITHUB_SECRET = 'ВАШИ ЗНАЧЕНИЯ'
EMAIL_HOST_PASSWORD = 'ВАШИ ЗНАЧЕНИЯ'
SECRET_KEY = 'ВАШИ ЗНАЧЕНИЯ'
```
5. Предварительно файл (.env) необходимо создать

6. Далее, нужно запустить проект что бы создалась база данных и сразу остановить при 
помощи сочетаний клавиш CTRL+C
``` python
python manage.py runserver
```
7. Затем нужно выполнить миграции
``` python
python manage.py migrate
```
8. Выполнить сбор статиики
``` python
python manage.py collectstatic
```
9. После чего можно запустить проект снова командой
``` python
python manage.py runserver
```
Проект будет доступен локально по адресу:
``` python
http://127.0.0.1:8000/
```