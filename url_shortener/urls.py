from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:short_url>/', views.redirect_original, name='redirect_original'),
    path('create_short_url/', views.create_short_url, name='create_short_url'),
    path('get_long_url/<str:short_url>/', views.get_long_url, name='get_long_url')
]