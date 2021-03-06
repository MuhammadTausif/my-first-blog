from django.urls import path
from . import views

urlpatterns = [
    # path('login', views.post_list, name='post_list'),
    # path('casual', views.casual, name='add_question'),
    path('add_question', views.add_question, name='add_question'),
    path('add_question_v', views.add_question_v, name='add_question_v'),
    path('questions_list', views.questions_list, name='questions_list'),
    path('users_list', views.users_list, name='users_list'),
    path('register_old', views.singup, name='signup'),
    path('register', views.singup, name='signup'),
    path('question', views.question, name='signup'),
    path('action', views.action, name='signup'),
    path('process', views.process, name='signup'),
    path('login', views.login_d, name='login_d'),
    path('singup', views.singup_d, name='singup_d'),
    path('', views.login_d, name='post_list'),
    # path('', views.post_list, name='post_list'),
]
