from urllib import request
from django.shortcuts import render
from .models import Blogpost

# Create your views here.


def index(request):
    '''I want this to be rendered as my landing page'''
    posted = Blogpost.objects.all()
    return render(request, 'index.html', {'posted': posted})


def content(request):
    '''Path to the content page'''
    return render(request, 'content.html')


def edit(request):
    '''For the editing page'''
    return render(request, 'edit.html')


def email(request):
    '''For the email path'''
    return render(request, 'edit.html')


def profile(request):
    '''For the profile page'''
    return render(request, 'profile.html')


def news_letter(request):
    '''When the click we want to see a display'''
    if request.method == 'POST':
        mail_check = request.POST.get('mailholder')
        print(mail_check)
    return render(request, 'index.html')
