from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('player', views.player, name='player'),
    path('search', views.search, name='search')
]