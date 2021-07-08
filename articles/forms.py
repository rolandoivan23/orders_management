from django.forms import ModelForm

from .models import Article 
class ArticleForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['vendors'].required = False

	class Meta:
		model = Article
		exclude = []