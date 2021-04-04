from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from article.models import Article


def home(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    num_pages = paginator.num_pages
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.page(num_pages)
    return render(request, 'blog/home.html', {'articles': page_obj})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'blog/login_user.html', {'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'blog/login_user.html', {'form': form, 'error': 'Either username or password is wrong!'})


def signup_user(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request, 'blog/signup_user.html', {'form': form})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'blog/signup_user.html', {'from': form, 'error': 'The passwords are not match.', })


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
