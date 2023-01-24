from django.shortcuts import render
from .models import News


def home_page(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request, 'blog/home.html', context)
