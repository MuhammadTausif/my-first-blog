from django.shortcuts import render

from blog.main_function import get_answer
from blog.nlp_project import login as main_login, singup as main_singup


# Create your views here.

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    temp_login_email = request.GET.get('email', '')
    temp_login_pass = request.GET.get('pass', '')
    temp_userName_pass = []
    temp_userName_pass.append(temp_login_email)
    temp_userName_pass.append(temp_login_pass)

    temp_response = main_login(temp_userName_pass)
    print('Response: '+temp_response)
    if(temp_response == 'login,Login OK'):
        return render(request, 'blog/question.html')
    return render(request, 'blog/post_list.html', {})

def login(request):
    return render(request, 'blog/login.html', {})

def singup(request):
    temp_email = request.GET.get('email', '')
    temp_pass = request.GET.get('pass', '')
    temp_user_pass = []
    temp_singup_message = ''
    if(len(temp_email) != 0 ):
        temp_user_pass.append(temp_email)
        temp_user_pass.append(temp_pass)
        temp_singup_message = main_singup(temp_user_pass)
        print(temp_singup_message)
    if(temp_singup_message == 'singup,Singup OK'):
        return render(request, 'blog/post_list.html', {})
        # return render(request, '/', {})
    elif(temp_singup_message == 'singup,Singup fialed'):
        return render(request, 'blog/singup.html', {'message':temp_singup_message})
    return render(request, 'blog/singup.html', {})

def process(request):
    from django import template

    register = template.Library()

    # temp_question = request.GET.get('question_text2', '')
    temp_question = request.GET.get('question', '')
    print('Question: {0}'.format(temp_question))
    print('Answer: {0}'.format(get_answer(temp_question)))
    temp_answer = get_answer(temp_question)

    # temp_answer = temp_question

    return render(request, 'blog/process.html', {'answer':temp_answer})

def question(request):
    return render(request, 'blog/question.html', {})

def action(request):
    return render(request, 'blog/action.html', {})
