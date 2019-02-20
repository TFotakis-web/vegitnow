from django.db import models


class Language(models.Model):
	Name = models.CharField(default='', max_length=100)
	Code = models.CharField(default='', max_length=10)

	def __str__(self): return self.Code + ': ' + self.Name


class StaticPage(models.Model):
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
	Content = models.TextField(blank=True)

	def __str__(self): return self.Name


class StaticPageTranslation(models.Model):
	StaticPage = models.ForeignKey(StaticPage, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
	Name = models.CharField(default='', max_length=1024)
	Content = models.TextField(blank=True)

	def __str__(self): return self.StaticPage.Name + ' -> ' + self.Name
