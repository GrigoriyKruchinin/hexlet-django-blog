from django.shortcuts import render


def index(request, tags='python', article_id=42):
    context = {
        'tags': tags,
        'article_id': article_id,
    }
    return render(request, 'articles/index.html', context)
