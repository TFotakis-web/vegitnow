from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import get_language

from general.models import Language


class Article(models.Model):
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	UploadDateTime = models.DateTimeField(auto_now_add=True, null=True)

	@property
	def LocalData(self):
		return ArticleContentTranslation.objects.filter(Article=self, Language__Code=get_language()).first()

	@property
	def LocalDataOrDefault(self):
		local = self.LocalData
		if local is None:
			return ArticleContentTranslation.objects.filter(Article=self).first()
		else:
			return local

	@property
	def Released(self):
		return self.LocalDataOrDefault.DoneEditing and (self.LocalDataOrDefault.ReleaseDateTime is None or self.LocalDataOrDefault.ReleaseDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple())

	def __str__(self):
		return self.LocalDataOrDefault.Title


class ArticleContentTranslation(models.Model):
	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
	Title = models.CharField(default='', blank=True, null=True, max_length=1024)
	Content = models.TextField(blank=True)
	Thumbnail = models.ImageField(default='Shared/defaultArticleThumbnail.png', upload_to='ArticleThumbnails/', blank=True)
	ReleaseDateTime = models.DateTimeField(default=None, blank=True, null=True)
	DoneEditing = models.BooleanField(default=False)

	@property
	def Released(self):
		return self.DoneEditing and (self.ReleaseDateTime is None or self.ReleaseDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple())

	@property
	def Preview(self):
		return self.Content[:130] + '...' if len(self.Content) > 130 else self.Content

	def __str__(self): return self.Language.Code + ': ' + self.Title


class ArticleType(models.Model):
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.Name + ' - ' + str(self.Language)


class ArticleTypeNameTranslation(models.Model):
	ArticleType = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.ArticleType.Name + ' -> ' + self.Language.Code + ': ' + self.Name


class ArticleTypeAssociation(models.Model):
	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	Type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)

	def __str__(self): return self.Type.Name + ': ' + self.Article.LocalDataOrDefault.Title


class Tag(models.Model):
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.Name + ' - ' + str(self.Language)


class TagNameTranslation(models.Model):
	Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.Tag.Name + ' -> ' + self.Language.Code + ': ' + self.Name


class TagAssociation(models.Model):
	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

	def __str__(self): return str(self.Article) + ' - ' + self.Tag.Name


def homePageArticles():
	articles = [article.LocalData for article in Article.objects.all()]
	return articles


def recommendedRecipes():
	pass


def recommendedArticles():
	pass
