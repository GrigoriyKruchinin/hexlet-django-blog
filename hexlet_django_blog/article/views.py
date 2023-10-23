from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    articles = ['Буратино утонул', 'Колобок повесился', 'Русалка села на шпагат']
    return render(request, 'articles/index.html', context={'articles': articles})