
from django.urls import path
from django.conf.urls import url, include
from articles.views import *

app_name = 'articles'
urlpatterns = [
    path('articles', ArticleListView.as_view(), name='articles-list'),
    path('articles/new/', ArticleCreateView.as_view(), name='article-new'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-show'),
    url(r'^', include('articles.api.urls')),
]
