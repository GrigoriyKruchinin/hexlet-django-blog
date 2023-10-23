version:
	poetry run django-admin version

start:
	python manage.py runserver

commands:
	python manage.py

# Создаем первые настройки нашего проекта
create_project:
	django-admin startproject hexlet_django_blog .

# Создать приложение (пакет с именем <article>). Для этого нужно находиться в пакете hexlet_django_blog
create_app:
	django-admin startapp article
