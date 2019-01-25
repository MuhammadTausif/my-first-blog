from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.singup, name='signup'),
    path('question', views.question, name='signup'),
    path('action', views.action, name='signup'),
    path('', views.post_list, name='post_list'),
]
