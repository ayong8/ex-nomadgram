from django.contrib import admin
from . import models

# Register your models here.

# 모델들이 어드민 패널에서 어떻게 보일지를 결정
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = (
		'file',
		'location',
		'caption',
		'created_at',
		'updated_at',
	)

	search_fields = (
		'location',
		'caption',
	)

	list_filter = (
		'location',
	)

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
	list_display = (
		'creator',
		'image',
		'created_at',
		'updated_at',
	)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
	# 어드민 패널에 보일 column 정의
	list_display = (
		'message',
		'creator',
		'image',
		'created_at',
		'updated_at',
	)