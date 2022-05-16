from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('content', views.content, name='content'),
    path('edit', views.edit, name='views'),
    path('email', views.email, name='email'),
    path('profile', views.profile, name='profile'),
    path('news_letter', views.news_letter, name='news_letter')
]
