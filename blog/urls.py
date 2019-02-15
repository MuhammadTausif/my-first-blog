from django.urls import path
from . import views

urlpatterns = [
    # path('login', views.post_list, name='post_list'),
    path('add_question', views.add_question, name='add_question'),
    path('add_question_v', views.add_question_v, name='add_question_v'),
    path('questions_list', views.questions_list, name='questions_list'),
    path('register', views.singup, name='signup'),
    path('question', views.question, name='signup'),
    path('action', views.action, name='signup'),
    path('process', views.process, name='signup'),
    path('', views.post_list, name='post_list'),
]
