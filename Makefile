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

# создаст миграцию 
migrations:
	python manage.py makemigrations

# посмотрим, какой SQL-запрос будет выполняться при запуске миграции
sqlmigrate:
	python manage.py sqlmigrate article 0001

# применим миграцию
migrate:
	python manage.py migrate

repl:
	python manage.py shell
