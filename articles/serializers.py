from rest_framework import serializers

from .models import Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'


class ArticleContentTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleContentTranslation
		fields = '__all__'


class ArticleTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleType
		fields = '__all__'


class ArticleTypeNameTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleTypeNameTranslation
		fields = '__all__'


class ArticleTypeAssociationSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleTypeAssociation
		fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'


class TagNameTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = TagNameTranslation
		fields = '__all__'


class TagAssociationSerializer(serializers.ModelSerializer):
	class Meta:
		model = TagAssociation
		fields = '__all__'
