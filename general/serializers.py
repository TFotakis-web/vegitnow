from rest_framework import serializers

from .models import Language, StaticPageTranslation, StaticPage, NewsletterUser


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = '__all__'


class StaticPageSerializer(serializers.ModelSerializer):
	class Meta:
		model = StaticPage
		fields = '__all__'


class StaticPageTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = StaticPageTranslation
		fields = '__all__'


class NewsletterUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsletterUser
		fields = '__all__'
