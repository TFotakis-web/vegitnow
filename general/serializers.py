from rest_framework import serializers

from .models import Language, StaticPageTranslation, StaticPage, NewsletterUser, Ad, AdTranslation


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


class AdSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ad
		fields = '__all__'


class AdTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdTranslation
		fields = '__all__'
