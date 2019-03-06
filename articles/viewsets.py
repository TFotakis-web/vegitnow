from datetime import datetime

from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import *

from general.models import Language
from .models import Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation, Ingredient, IngredientNameTranslation, IngredientAssociation, Unit, UnitNameTranslation  # , UnitAssociation
from .serializers import ArticleSerializer, ArticleContentTranslationSerializer, ArticleTypeSerializer, ArticleTypeNameTranslationSerializer, ArticleTypeAssociationSerializer, TagSerializer, TagNameTranslationSerializer, TagAssociationSerializer, IngredientSerializer, IngredientNameTranslationSerializer, IngredientAssociationSerializer, UnitSerializer, UnitNameTranslationSerializer  # , UnitAssociationSerializer


class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleContentTranslationViewSet(viewsets.ModelViewSet):
	queryset = ArticleContentTranslation.objects.all()
	serializer_class = ArticleContentTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleTypeViewSet(viewsets.ModelViewSet):
	queryset = ArticleType.objects.all()
	serializer_class = ArticleTypeSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleTypeNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = ArticleTypeNameTranslation.objects.all()
	serializer_class = ArticleTypeNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleTypeAssociationViewSet(viewsets.ModelViewSet):
	queryset = ArticleTypeAssociation.objects.all()
	serializer_class = ArticleTypeAssociationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class TagNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = TagNameTranslation.objects.all()
	serializer_class = TagNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class TagAssociationViewSet(viewsets.ModelViewSet):
	queryset = TagAssociation.objects.all()
	serializer_class = TagAssociationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class IngredientViewSet(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		queryset = Ingredient.objects.all()
		serializer = self.get_serializer(queryset, many=True)
		data = {}
		for obj in serializer.data:
			data[obj['id']] = obj
		return Response(data)


class IngredientNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = IngredientNameTranslation.objects.all()
	serializer_class = IngredientNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		sd = serializer.data
		data = {}
		for lang in Language.objects.all():
			data[lang.id] = {}
			for obj in sd:
				if obj['Language'] == lang.id:
					data[lang.id][obj['Ingredient']] = obj['Name']
		return Response(data)


class IngredientAssociationViewSet(viewsets.ModelViewSet):
	queryset = IngredientAssociation.objects.all()
	serializer_class = IngredientAssociationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def retrieve(self, request, *args, **kwargs):
		queryset = IngredientAssociation.objects.filter(Article_id=kwargs['pk']).order_by('-IsMainIngredient')
		serializer = self.get_serializer(queryset, many=True)
		data = serializer.data
		return Response(data)


class UnitViewSet(viewsets.ModelViewSet):
	queryset = Unit.objects.all()
	serializer_class = UnitSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class UnitNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = UnitNameTranslation.objects.all()
	serializer_class = UnitNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class NewArticleViewSet(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
	permission_classes = (IsAdminUser,)

	def create(self, request, *args, **kwargs):
		a = Article(User=User.objects.filter(is_superuser=True).first())
		a.save()
		at = request.data['articleType']
		translations = request.data['translations']
		ata = ArticleTypeAssociation(Article=a, Type_id=at)
		ata.save()
		for translation in translations:
			act = ArticleContentTranslation(Article=a, Language_id=translation['language'])
			act.Title = translation['title']
			act.Content = translation['content']
			act.Thumbnail = translation['thumbnail']
			dateStr = translation['releaseDateTime']['date'] + '-' + translation['releaseDateTime']['time'] + '-' + 'UTC'
			act.ReleaseDateTime = datetime.strptime(dateStr, '%d/%m/%Y-%H:%M-%Z')
			act.DoneEditing = translation['doneEditing']
			soup = BeautifulSoup(translation['content'], features='html.parser')
			rawText = soup.get_text()
			act.Preview = (rawText[:100] if len(rawText) > 100 else rawText) + '...'
			if at == 1:
				act.Dishes = request.data['dishes']
				act.ReadyIn = request.data['readyIn']
				act.YoutubeLink = request.data['youtubeLink']
			elif at == 2:
				act.AuthorName = translation['authorName']
				act.AuthorProfession = translation['authorProfession']
			act.save()
		if at == 1:
			ingredients = request.data['ingredients']
			for ingredient in ingredients:
				ia = IngredientAssociation(Article=a, Ingredient_id=ingredient['ingredientId'], Quantity=ingredient['quantity'], IsMainIngredient=ingredient['isMainIngredient'])
				ia.save()
		return Response(status=HTTP_201_CREATED)


class NewIngredientViewSet(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
	permission_classes = (IsAdminUser,)

	def create(self, request, **kwargs):
		ingredient = Ingredient(
			Name=request.data['English'],
			Language=Language.objects.get(Code='en'),
			Calories=request.data['Calories'],
			Protein=request.data['Protein'],
			CarbonHydrates=request.data['CarbonHydrates'],
			Fats=request.data['Fats'],
			VitaminA=request.data['VitaminA'],
			CarotinB=request.data['CarotinB'],
			VitaminC=request.data['VitaminC'],
			VitaminD=request.data['VitaminD'],
			VitaminE=request.data['VitaminE'],
			VitaminK=request.data['VitaminK'],
			VitaminB3=request.data['VitaminB3'],
			VitaminB6=request.data['VitaminB6'],
			VitaminB12=request.data['VitaminB12'],
			VitaminB9=request.data['VitaminB9'],
			Choline=request.data['Choline'],
			Calcium=request.data['Calcium'],
			Iron=request.data['Iron'],
			Magnesium=request.data['Magnesium'],
			Phosphorus=request.data['Phosphorus'],
			Potassium=request.data['Potassium'],
			Sodium=request.data['Sodium'],
			Zinc=request.data['Zinc'],
			Selenium=request.data['Selenium'],
			Manganese=request.data['Manganese'],
			Water=request.data['Water'],
		)
		ingredient.save()
		ingredientTranslation = IngredientNameTranslation(
			Ingredient=ingredient,
			Name=request.data['Greek'],
			Language=Language.objects.get(Code='el')
		)
		ingredientTranslation.save()
		return Response(status=HTTP_201_CREATED)

	def update(self, request, *args, **kwargs):
		Ingredient.objects.filter(id=kwargs['pk']).update(
			Name=request.data['English'],
			Calories=request.data['Calories'],
			Protein=request.data['Protein'],
			CarbonHydrates=request.data['CarbonHydrates'],
			Fats=request.data['Fats'],
			VitaminA=request.data['VitaminA'],
			CarotinB=request.data['CarotinB'],
			VitaminC=request.data['VitaminC'],
			VitaminD=request.data['VitaminD'],
			VitaminE=request.data['VitaminE'],
			VitaminK=request.data['VitaminK'],
			VitaminB3=request.data['VitaminB3'],
			VitaminB6=request.data['VitaminB6'],
			VitaminB12=request.data['VitaminB12'],
			VitaminB9=request.data['VitaminB9'],
			Choline=request.data['Choline'],
			Calcium=request.data['Calcium'],
			Iron=request.data['Iron'],
			Magnesium=request.data['Magnesium'],
			Phosphorus=request.data['Phosphorus'],
			Potassium=request.data['Potassium'],
			Sodium=request.data['Sodium'],
			Zinc=request.data['Zinc'],
			Selenium=request.data['Selenium'],
			Manganese=request.data['Manganese'],
			Water=request.data['Water'],
		)
		IngredientNameTranslation.objects.filter(Ingredient_id=kwargs['pk']).update(Name=request.data['Greek'])
		return Response(status=HTTP_206_PARTIAL_CONTENT)
