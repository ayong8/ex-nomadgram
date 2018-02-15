from django.db import models
from django.utils.coding import python_2_unicode_compatible
from nomadgram.users import models as user_models

class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True) # Whenever an instance is created, it's automatically generated
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:	# Define it as abstract class
		abstract = True

class Image(TimeStampedModel):
	file = models.ImageField()
	location = models.CharField(max_length=140)
	caption = models.TextField()
	creator = models.ForeignKey(user_models.User, null=True)

	def __str__(self):
		# string의 형식(representation)이 어떻게 보일 것인가 ... seoul - captial of korea (값 사이에 짝대기를 넣는다)
		return '{} - {}'.format(self.location, self.caption)

class Comment(TimeStampedModel):
	message = models.TextField()
	creator = models.ForeignKey(user_models.User, null=True)
	image = models.ForeignKey(Image, null=True)

	def __str__(self):
		return self.message

class Like(TimeStampedModel):
	creator = models.ForeignKey(user_models.User)
	image = models.ForeignKey(Image)

	def __str__(self):
		return 'User:{} - Image:{}'.format(self.creator.username, self.image.caption)