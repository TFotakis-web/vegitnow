from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from general.models import Language
from froala_editor.fields import FroalaField


class ArticleType(models.Model):
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.Name + ' - ' + str(self.Language)


class Article(models.Model):
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	UploadDateTime = models.DateTimeField(auto_now_add=True, null=True)
	ArticleType = models.ForeignKey(ArticleType, on_delete=models.CASCADE)

	def __str__(self):
		translation = self.articlecontenttranslation_set.first()
		return translation.Title if translation else 'Default Title'


class ArticleContentTranslation(models.Model):
	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
	Title = models.CharField(default='', blank=True, null=True, max_length=1024)
	Preview = models.CharField(default='', blank=True, null=True, max_length=150)
	Content = FroalaField(blank=True)
	Thumbnail = models.ImageField(blank=True, upload_to='articles')
	ReleaseDateTime = models.DateTimeField(default=None, blank=True, null=True)
	DoneEditing = models.BooleanField(default=False)
	Dishes = models.IntegerField(default=0)
	Cooking = models.IntegerField(default=0)
	Preparation = models.IntegerField(default=0)
	Waiting = models.IntegerField(default=0)
	YoutubeLink = models.CharField(default='', blank=True, null=True, max_length=1024)
	AuthorName = models.CharField(default='', blank=True, null=True, max_length=1024)
	AuthorProfession = models.CharField(default='', blank=True, null=True, max_length=1024)
	AuthorProfilePicture = models.ImageField(blank=True, upload_to='articles')
	OnCarousel = models.BooleanField(default=False)

	@property
	def Released(self):
		return self.DoneEditing and (self.ReleaseDateTime is None or self.ReleaseDateTime.utctimetuple() <= datetime.now().astimezone().utctimetuple())

	def __str__(self): return self.Language.Code + ': ' + self.Title


class ArticleTypeNameTranslation(models.Model):
	ArticleType = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.ArticleType.Name + ' -> ' + self.Language.Code + ': ' + self.Name


class ArticleTypeAssociation(models.Model):
	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	Type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)

	def __str__(self): return self.Type.Name + ': ' + str(self.Article)


class Ingredient(models.Model):
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
	Calories = models.FloatField(default=0)
	Protein = models.FloatField(default=0)
	CarbonHydrates = models.FloatField(default=0)
	Fats = models.FloatField(default=0)
	VitaminA = models.FloatField(default=0)
	CarotinB = models.FloatField(default=0)
	VitaminC = models.FloatField(default=0)
	VitaminD = models.FloatField(default=0)
	VitaminE = models.FloatField(default=0)
	VitaminK = models.FloatField(default=0)
	VitaminB3 = models.FloatField(default=0)
	VitaminB6 = models.FloatField(default=0)
	VitaminB12 = models.FloatField(default=0)
	VitaminB9 = models.FloatField(default=0)
	Choline = models.FloatField(default=0)
	Calcium = models.FloatField(default=0)
	Iron = models.FloatField(default=0)
	Magnesium = models.FloatField(default=0)
	Phosphorus = models.FloatField(default=0)
	Potassium = models.FloatField(default=0)
	Sodium = models.FloatField(default=0)
	Zinc = models.FloatField(default=0)
	Selenium = models.FloatField(default=0)
	Manganese = models.FloatField(default=0)
	Water = models.FloatField(default=0)

	def __str__(self): return self.Name + ' - ' + str(self.Language)


class IngredientNameTranslation(models.Model):
	Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	Name = models.CharField(default='', max_length=1024)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self): return self.Ingredient.Name + ' -> ' + self.Language.Code + ': ' + self.Name


class IngredientAssociation(models.Model):
	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
	Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	Quantity = models.FloatField(default=0)
	IsMainIngredient = models.BooleanField(default=False)

	def __str__(self): return str(self.Article) + ' - ' + self.Ingredient.Name


# class TmpImages(models.Model):
# 	image = models.ImageField()
#
# 	def __str__(self):
# 		return str(self.image)


# @receiver(post_delete, sender=TmpImages)
def auto_delete_file_on_model_delete(sender, field, instance, **kwargs):
	instance[field].delete(False)


# @receiver(pre_save, sender=TmpImages)
def auto_delete_on_file_change(sender, instance, **kwargs):
	if not instance.pk:
		return False
	old_file = sender.objects.get(pk=instance.pk).image
	old_file.delete(False)

# class Tag(models.Model):
# 	Name = models.CharField(default='', max_length=1024)
# 	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
#
# 	def __str__(self): return self.Name + ' - ' + str(self.Language)
#
#
# class TagNameTranslation(models.Model):
# 	Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
# 	Name = models.CharField(default='', max_length=1024)
# 	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
#
# 	def __str__(self): return self.Tag.Name + ' -> ' + self.Language.Code + ': ' + self.Name
#
#
# class TagAssociation(models.Model):
# 	Article = models.ForeignKey(Article, on_delete=models.CASCADE)
# 	Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#
# 	def __str__(self): return str(self.Article) + ' - ' + self.Tag.Name
#
#
# class Unit(models.Model):
# 	Name = models.CharField(default='', max_length=1024)
# 	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
#
# 	def __str__(self): return self.Name + ' - ' + str(self.Language)
#
#
# class UnitNameTranslation(models.Model):
# 	Unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
# 	Name = models.CharField(default='', max_length=1024)
# 	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
#
# 	def __str__(self): return self.Unit.Name + ' -> ' + self.Language.Code + ': ' + self.Name
#
#
# class UnitAssociation(models.Model):
# 	Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
# 	Unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
#
# 	def __str__(self): return str(self.Ingredient) + ' - ' + self.Unit.Name
