from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from general.models import Language


class Role(models.Model):
	Name = models.CharField(default='', max_length=100)

	def __str__(self): return self.Name


class Profile(models.Model):
	User = models.OneToOneField(User, on_delete=models.CASCADE)
	Role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, default=3)
	ProfilePhoto = models.ImageField(default='Shared/defaultProfilePicture.png', upload_to='ProfilePictures/', blank=True)

	@property
	def FullName(self): return self.User.first_name + ' ' + self.User.last_name

	def __str__(self): return self.FullName


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(User=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
