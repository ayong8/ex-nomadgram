from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):

	class Meta:
		model = models.Image
		fields = '__all__'


class CommentSerializer(serializers.Serializer):

	class Meta:
		model = models.Comment
		fields = '__all__'   # all of them


class LikeSerializer(serializers.Serializer):

	class Meta:
		models = models.like
		fields = '__all__'