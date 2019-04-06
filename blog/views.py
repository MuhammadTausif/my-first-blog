from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db import IntegrityError

from blog.main_function import get_answer
from blog.question_function import get_questions, add_question_func, add_question_on_hold, get_questions_on_hold
from blog.nlp_project import login as main_login, singup as main_singup
from django.contrib.auth import authenticate, login

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
        return redirect('/question')
        # return render(request, 'blog/question.html')
    return render(request, 'blog/post_list.html', {})

def login_d(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    temp_login_email = request.GET.get('email', '')
    temp_login_pass = request.GET.get('pass', '')
    user = authenticate(request, username=temp_login_email, password=temp_login_pass)
    if user is not None:
        return redirect('/question')
        # return render(request, 'blog/question.html')
    return render(request, 'blog/login_d.html', {})

def singup_d(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('firstname', '')
            last_name = request.POST.get('lastname', '')
            temp_email = request.POST.get('email', '')
            temp_pass = request.POST.get('pass', '')
            user = User.objects.create_user(temp_email, temp_email, temp_pass)
            print(first_name + ' : ' + last_name)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            # user already exists
            status = 'user already exists'
            return render(request, 'blog/singup_d.html', { 'status': status })
        else:
            status = 'new user was created'
            return redirect('/login')

    return render(request, 'blog/singup_d.html', {})

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
        # return render(request, 'blog/post_list.html', {})
        return redirect('/')
        # return render(request, '/', {})
    elif(temp_singup_message == 'singup,Singup fialed'):
        return render(request, 'blog/singup.html', {'message':temp_singup_message})
    return render(request, 'blog/singup.html', {})

def process(request):
    from django import template

    register = template.Library()

    # temp_question = request.GET.get('question_text2', '')
    temp_question = request.GET.get('question', '')
    # print('Question: {0}'.format(temp_question))
    # print('Answer: {0}'.format(get_answer(temp_question)))
    temp_answer = get_answer(temp_question)
    if temp_answer == False:
        temp_answer = "Your question is put on hold and would be answered ASAP. please."
        add_question_on_hold(temp_question)
    # temp_answer = temp_question

    return render(request, 'blog/process.html', {'answer':temp_answer})

def question(request):
    return render(request, 'blog/question.html', {})

def action(request):
    return render(request, 'blog/action.html', {})

def add_question_v(request):
    return render(request, 'blog/add_question_v.html')

def add_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        category = request.POST.get('category')
        parameter1 = request.POST.get('parameter1')
        parameter2 = request.POST.get('parameter2')
        keyword1 = request.POST.get('keyword1')
        keyword2 = request.POST.get('keyword2')
        print('Values:\n Q' + question +
              '\nA: '+ answer+
              '\nP1: '+ parameter1+
              '\nP2: '+ parameter2+
              '\nk1: '+ keyword1+
              '\nk2: '+ keyword2 +
              '\nc: '+category
              )
        add_question_func(question,parameter1,parameter2,keyword1,keyword2,answer, category)
        # Redirectiong to list
        contacts_orignal = get_questions('0', '20000')
        page = request.GET.get('page')
        contacts_paginator = Paginator(contacts_orignal, 5)
        contacts = contacts_paginator.get_page(page)

        # return render(request, 'blog/questions_list.html', {'contacts': contacts})
        return redirect('/questions_list')
    return render(request, 'blog/add_question.html', {})

def questions_list(request):

    # Working code
    questions = get_questions('0','100')
    paginator = Paginator(questions, 5)  # Show 25 contacts per page
    questions = paginator.get_page(1)
    questions_dict = {i: list(questions[i]) for i in range(0, len(questions))}

    # Sample code
    contacts_orignal = get_questions('0','20000')
    page = request.GET.get('page')
    contacts_paginator = Paginator(contacts_orignal, 5)
    contacts = contacts_paginator.get_page(page)

    if page :
        contacts = contacts_paginator.get_page(page)
    else:
        contacts = contacts_paginator.get_page(contacts.paginator.num_pages)

    return render(request, 'blog/questions_list.html', {'questions_dict':questions_dict, 'contacts': contacts})

def users_list(request):

    # Working code
    questions = get_questions('0','100')
    paginator = Paginator(questions, 5)  # Show 25 contacts per page
    questions = paginator.get_page(1)
    questions_dict = {i: list(questions[i]) for i in range(0, len(questions))}

    # Sample code
    contacts_orignal = get_questions('0','20000')
    contacts_orignal = User.objects.all();
    page = request.GET.get('page')
    contacts_paginator = Paginator(contacts_orignal, 5)
    contacts = contacts_paginator.get_page(page)

    if page :
        contacts = contacts_paginator.get_page(page)
    else:
        contacts = contacts_paginator.get_page(contacts.paginator.num_pages)

    return render(request, 'blog/users_list.html', {'questions_dict':questions_dict, 'contacts': contacts})

def questions_list_onhold(request):

    # Working code
    questions = get_questions_on_hold()
    paginator = Paginator(questions, 5)  # Show 25 contacts per page
    questions = paginator.get_page(1)
    questions_dict = {i: list(questions[i]) for i in range(0, len(questions))}

    # Sample code
    contacts_orignal = get_questions_on_hold()
    page = request.GET.get('page')
    contacts_paginator = Paginator(contacts_orignal, 5)
    contacts = contacts_paginator.get_page(page)

    if page :
        contacts = contacts_paginator.get_page(page)
    else:
        contacts = contacts_paginator.get_page(contacts.paginator.num_pages)

    return render(request, 'blog/questions_list_onhold.html', {'questions_dict':questions_dict, 'contacts': contacts})

# def casual(request):
#     return render(request, 'blog/casual/login.html', {})

