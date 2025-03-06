from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_words/', views.check_words, name='check_words'),
    path('requirements/', views.requirements, name='requirements'),
]