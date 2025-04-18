from django.urls import path

from .views import HomeView, ShortenUrlView

urlpatterns = [
    path('<slug:slug>', HomeView.as_view(), name='url-redirect'),
    path('shorten/', ShortenUrlView.as_view(), name='shorten')
    # path('<slug:shortened_url>/', name='redirect_to_original_url')
]
