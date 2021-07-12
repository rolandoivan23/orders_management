from django.test import TestCase
from articles.models import *

# Create your tests here.
class AtriclesTests(TestCase):

	def test_article_get_absolute_url(self):
		article = Article.objects.last()
		if article is None: 
			article = Article.objects.create(code = 'Some code', 
							  description = 'Just for testing propouses',
							  price = 199.99)
		article_url = article.get_absolute_url()
		self.assertEqual(article_url, "/article/%d/" % (article.pk,))
		self.assertTrue(article_url != "/article/%d" % (article.pk,))
		self.assertTrue(article_url != "article/%d/" % (article.pk,))
		self.assertTrue(article_url != "article/%d" % (article.pk,))

	def test_article_1_exists(self):
		article_exists = Article.objects.filter(pk = 1).exists()
		self.assertTrue(article_exists)
		