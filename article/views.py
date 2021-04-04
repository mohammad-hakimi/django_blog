from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from article.forms import ArticleForm
from article.models import Article


@login_required
def create_article(request):
    form = ArticleForm()
    if request.method == 'GET':
        return render(request, 'article/create_article.html', {'form': form})
    else:
        try:
            article_form = ArticleForm(request.POST, request.FILES)
            article_temp = article_form.save(commit=False)
            article_temp.user = request.user
            article_temp.date_created = timezone.now()
            article_temp.save()
            return redirect('home')
        except ValueError:
            return render(request, 'article/create_article.html', {'form': form, 'error': 'Entered values are wrong!'})


def show_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article/show_article.html', {'article': article})


@login_required
def user_articles(request):
    articles = Article.objects.all().filter(user_id=request.user.id)
    return render(request, 'blog/home.html', {'articles': articles})
