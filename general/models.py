from django.db import models


class Language(models.Model):
	Name = models.CharField(default='', max_length=100)
	Code = models.CharField(default='', max_length=10)

	def __str__(self): return self.Code + ': ' + self.Name
