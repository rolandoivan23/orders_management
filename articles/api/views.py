from .serializers import *
from rest_framework import viewsets

from articles.models import Article
# Create your views here.
class ArticlesViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer