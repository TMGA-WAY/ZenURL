from django.shortcuts import render
from django.shortcuts import redirect


from .service import shortener_service


# Create your views here.

def home(request):
    return render(request, 'url_shortener/home.html')


def redirect_original(request, short_url):
    long_url = shortener_service.fetch_url(url=short_url, user_id=None, is_long=False)
    if long_url is not "PROPER":  # TODO: Implement the check
        return render(request, 'url_shortener/home.html')
    return redirect(long_url)


def create_short_url(request):
    long_url = request.POST.get('long_url')
    print("Long URL: ", long_url)
    short_url = shortener_service.save_short_url(long_url=long_url, user_id=None, is_public=True)
    return render(request, 'url_shortener/home.html')


def get_long_url(request, short_url):
    long_url = shortener_service.fetch_url(url=short_url, user_id=None, is_long=False)
    return render(request, 'url_shortener/home.html')
