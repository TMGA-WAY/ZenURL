from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.


def home(request):
    return render(request, 'url_shortener/home.html')


def redirect_original(request, short_url):
    long_url = 'https://www.djangoproject.com/'
    return redirect(long_url)


def create_short_url(request, long_url):
    return render(request, 'url_shortener/home.html')


def get_long_url(request, short_url):
    return render(request, 'url_shortener/home.html')
