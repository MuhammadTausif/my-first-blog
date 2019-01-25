from django.shortcuts import render
from django.utils import timezone
from blog.nlp_project import login as main_login

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    temp_email = request.GET.get('email', '')
    temp_pass = request.GET.get('pass', '')
    print('Email: {0}'.format(temp_email))
    print('Pass: {0}'.format(temp_pass))
    print('Res')
    temp_userName_pass = []
    temp_userName_pass.append(temp_email)
    temp_userName_pass.append(temp_pass)

    temp_response = main_login(temp_userName_pass)
    print('Response: '+temp_response)
    if(temp_response == 'login,Login OK'):
        return render(request, 'blog/question.html')
    return render(request, 'blog/post_list.html', {'posts': posts})

def login(request):
    return render(request, 'blog/login.html', {})

def singup(request):
    return render(request, 'blog/singup.html', {})

def process(request):
    return render(request, 'blog/process.html', {})

def question(request):
    return render(request, 'blog/question.html', {})

