from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


def about(request):
    return render(request, 'about.html')


def redirect_to_article(request):
    # Создаем URL для перенаправления с помощью reverse
    redirect_url = reverse('article', args=('python', 42))
    # Используем функцию redirect для выполнения перенаправления
    return redirect(redirect_url)

def index(request):
    return render(request, 'index.html')