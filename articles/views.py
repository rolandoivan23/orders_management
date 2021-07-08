from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ArticleForm
from .models import *

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article

class ArticleCreateView(CreateView):
	model = Article
	namespace = 'articles'
	#fields = ['code', 'description', 'price']
	form_class = ArticleForm
	

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name_suffix = '_update_form'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:articles-list')