from rest_framework import serializers

from articles.models import Article
from articles.models import ArticleContentTranslation
from articles.models import ArticleType
from articles.models import ArticleTypeAssociation
from articles.models import ArticleTypeNameTranslation
from articles.models import Ingredient
from articles.models import IngredientAssociation
from articles.models import IngredientNameTranslation


# from articles.models import Tag
# from articles.models import TagNameTranslation
# from articles.models import TagAssociation
# from articles.models import Unit
# from articles.models import UnitNameTranslation
# from articles.models import UnitAssociation


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


class IngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ingredient
		fields = '__all__'


class IngredientNameTranslationSerializer(serializers.ModelSerializer):
	class Meta:
		model = IngredientNameTranslation
		fields = '__all__'


class IngredientAssociationSerializer(serializers.ModelSerializer):
	class Meta:
		model = IngredientAssociation
		fields = '__all__'

#
# class TagSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Tag
# 		fields = '__all__'
#
#
# class TagNameTranslationSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = TagNameTranslation
# 		fields = '__all__'
#
#
# class TagAssociationSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = TagAssociation
# 		fields = '__all__'
#
#
# class UnitSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Unit
# 		fields = '__all__'
#
#
# class UnitNameTranslationSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = UnitNameTranslation
# 		fields = '__all__'
#
# class UnitAssociationSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = UnitAssociation
# 		fields = '__all__'
