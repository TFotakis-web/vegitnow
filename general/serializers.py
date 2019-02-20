from rest_framework import serializers

from .models import Language, StaticPageTranslation, StaticPage


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
