from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='post_list'),
    path('register', views.singup, name='signup'),
    path('question', views.question, name='signup'),
    path('action', views.action, name='signup'),
    path('process', views.process, name='signup'),
    path('', views.post_list, name='post_list'),
]
