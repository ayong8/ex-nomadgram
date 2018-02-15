from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
	""" User model """


	GENDER_CHOICES = (
		('male', 'Male'),
		('female', 'Female'),
		('not-specified', 'Not specified')
	)

	name = models.CharField(_('Name of User'), blank=True, max_length=255)
	website = models.URLField(null=True) # null=True... 디폴트값을 남기기 위함
	bio = models.TextField(null=True)
	phone = models.CharField(max_length=140, null=True)
	gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
	followers = models.ManyToManyField("self")	# user to user이므로 해당 클래스 user을 참조
	following = models.ManyToManyField("self")

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse('users:detail', kwargs={'username': self.username})