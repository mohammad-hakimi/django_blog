"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views
from article import views as article_views
from django_blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/signup', views.signup_user, name='signup_user'),
    path('auth/logout', views.logout_user, name='logout_user'),
    path('article/create/', article_views.create_article, name='create_article'),
    path('article/article/<int:article_id>', article_views.show_article, name='show_article'),
    path('user/articles/', article_views.user_articles, name='user_articles'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
