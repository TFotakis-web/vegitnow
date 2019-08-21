from django.db import models
from datetime import datetime
from enum import Enum


class Language(models.Model):
	Name = models.CharField(default='', max_length=100)
	Code = models.CharField(default='', max_length=10)

	def __str__(self): return self.Code + ': ' + self.Name


class StaticPage(models.Model):
	Main = models.ForeignKey('StaticPageTranslation', blank=True, null=True, on_delete=models.DO_NOTHING)

	def __str__(self): return self.Main.Name


class StaticPageTranslation(models.Model):
	StaticPage = models.ForeignKey(StaticPage, blank=True, null=True, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
	Name = models.CharField(default='', max_length=1024)
	Content = models.TextField(blank=True)
	# Todo: Make single field (Listed/Unlisted/Private)
	Listed = models.BooleanField(default=False)
	Private = models.BooleanField(default=True)

	def __str__(self): return self.Name


class NewsletterUser(models.Model):
	email = models.CharField(default='', max_length=254)
	SubscribeDateTime = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.email


class AdTranslation(models.Model):
	Ad = models.ForeignKey('Ad', blank=True, null=True, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
	Image = models.ImageField(blank=True, upload_to='vegitnowads')
	Link = models.CharField(default='', max_length=2048)

	def __str__(self): return self.Ad.Name + ': ' + self.Language.Code


class AdTypeEnum(Enum):
	HOME_JOIN_OUR_FAMILY = 'Home: Join Our Family'
	HOME_ARTICLES = 'Home: Articles'
	HOME_RECIPES = 'Home: Recipes'
	INSIDE_POST = 'Inside: Post'


class Ad(models.Model):
	Name = models.CharField(default='', max_length=100)
	AdType = models.CharField(
		max_length=50,
		choices=[(tag.name, tag.value) for tag in AdTypeEnum]
	)
	Clicks = models.IntegerField(default=0, blank=True)
	TargetClicks = models.IntegerField(default=0, blank=True)
	ReleaseDateTime = models.DateTimeField(default=None, blank=True, null=True)
	RemoveDateTime = models.DateTimeField(default=None, blank=True, null=True)

	@property
	def Active(self):
		released = self.ReleaseDateTime is None or self.ReleaseDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()
		clicksRemaining = self.Clicks < self.TargetClicks
		removed = self.RemoveDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple()
		return released and clicksRemaining and not removed

	def __str__(self): return self.Name
