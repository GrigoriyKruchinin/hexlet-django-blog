from django.shortcuts import render
from django.views import View

# Create your views here.
from django.http import HttpResponse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = ['Буратино утонул', 'Колобок повесился', 'Русалка села на шпагат']
        return render(request, 'articles/index.html', context={'articles': articles})