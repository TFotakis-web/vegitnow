from bs4 import BeautifulSoup
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import *

from articles.models import Article
from articles.models import ArticleContentTranslation
from articles.models import ArticleType
from articles.models import ArticleTypeAssociation
from articles.models import ArticleTypeNameTranslation
from articles.models import Ingredient
from articles.models import IngredientAssociation
from articles.models import IngredientNameTranslation
from general.models import Language
from .serializers import ArticleContentTranslationSerializer
from .serializers import ArticleSerializer
from .serializers import ArticleTypeAssociationSerializer
from .serializers import ArticleTypeNameTranslationSerializer
from .serializers import ArticleTypeSerializer
from .serializers import IngredientAssociationSerializer
from .serializers import IngredientNameTranslationSerializer
from .serializers import IngredientSerializer


# from articles.models import Tag
# from articles.models import TagNameTranslation
# from articles.models import TagAssociation
# from articles.models import Unit
# from articles.models import UnitNameTranslation
# from articles.models import UnitAssociation
# from articles.serializers import TagSerializer
# from articles.serializers import TagNameTranslationSerializer
# from articles.serializers import TagAssociationSerializer
# from articles.serializers import UnitSerializer
# from articles.serializers import UnitNameTranslationSerializer
# from articles.serializers import UntAssociationSerializer


def base64toFile(filename, data):
	import base64
	from django.core.files.base import ContentFile
	fileFormat, fileData = data.split(';base64,')
	ext = fileFormat.split('/')[-1]
	contentFile = ContentFile(base64.b64decode(fileData), name=filename)
	return contentFile


class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def retrieve(self, request, *args, **kwargs):
		if not kwargs['pk'].isdigit():
			return Response(status=HTTP_400_BAD_REQUEST)
		article = Article.objects.filter(id=kwargs['pk']).first()
		if not article:
			return Response(status=HTTP_404_NOT_FOUND)
		fTranslations = {}
		if 'locale' in request.query_params:
			fTranslations['Language_id'] = int(request.query_params['locale'])

		translations = article.articlecontenttranslation_set.filter(**fTranslations).all()
		if not translations:
			return Response(status=HTTP_404_NOT_FOUND)

		if 'edit' in request.query_params:
			data = {
				'id': kwargs['pk'],
				'ArticleTypeId': article.ArticleType_id,
				'Translations': []
			}
			for translation in translations:
				translationData = {
					'id': translation.id,
					'Title': translation.Title,
					'Preview': translation.Preview,
					'Content': translation.Content,
					'Thumbnail': {
						'name': '',
						'data': '',
						'url': translation.Thumbnail.url
					},
					'ReleaseDateTime': {
						'date': translation.ReleaseDateTime.strftime('%d/%m/%Y'),
						'time': translation.ReleaseDateTime.strftime('%H:%M')
					},
					'Language': translation.Language_id,
					'OnCarousel': translation.OnCarousel,
					'DoneEditing': translation.DoneEditing
				}
				if data['ArticleTypeId'] == 2:
					translationData['AuthorName'] = translation.AuthorName
					translationData['AuthorProfession'] = translation.AuthorProfession
					translationData['AuthorProfilePicture'] = {'name': '', 'data': '', 'url': translation.AuthorProfilePicture.url},
				data['Translations'].append(translationData)
			if data['ArticleTypeId'] == 1:
				data['Dishes'] = translations.first().Dishes
				data['Cooking'] = translations.first().Cooking
				data['Preparation'] = translations.first().Preparation
				data['Waiting'] = translations.first().Waiting
				data['YoutubeLink'] = translations.first().YoutubeLink
				data['Ingredients'] = []
				ingredientList = IngredientAssociation.objects.filter(Article_id=kwargs['pk']).all()
				for ingredient in ingredientList:
					ingredientData = {
						'id': ingredient.id,
						'Ingredient': ingredient.Ingredient_id,
						'Quantity': ingredient.Quantity,
						'IsMainIngredient': ingredient.IsMainIngredient
					}
					data['Ingredients'].append(ingredientData)
			return Response(data)

		translation = translations.first()
		data = {
			'id': translation.id,
			'Title': translation.Title,
			'Preview': translation.Preview,
			'Content': translation.Content,
			'Thumbnail': translation.Thumbnail.url,
			'ReleaseDateTime': {
				'date': translation.ReleaseDateTime.strftime('%d/%m/%Y'),
				'time': translation.ReleaseDateTime.strftime('%H:%M')
			},
			'YoutubeLink': translation.YoutubeLink,
			'Language': translation.Language_id,
			'OnCarousel': translation.OnCarousel,
			'DoneEditing': translation.DoneEditing
		}
		if translation.Article.ArticleType_id == 1:
			data.update({
				'Dishes': translation.Dishes,
				'Cooking': translation.Cooking,
				'Preparation': translation.Preparation,
				'Waiting': translation.Waiting,
			})
			ingredientList = IngredientAssociation.objects.filter(Article_id=kwargs['pk']).all()
			data['Ingredients'] = []
			for ingredient in ingredientList:
				ingredientData = {
					'Name': ingredient.Ingredient.Name,
					'Quantity': ingredient.Quantity,
					'IsMainIngredient': ingredient.IsMainIngredient
				}
				if 'locale' in request.query_params:
					if ingredient.Ingredient.Language_id != int(request.query_params['locale']):
						ingredientData['Name'] = ingredient.Ingredient.ingredientnametranslation_set.filter(**fTranslations).first().Name
				data['Ingredients'].append(ingredientData)

		if translation.Article.ArticleType_id == 2:
			data.update({
				'AuthorName': translation.AuthorName,
				'AuthorProfession': translation.AuthorProfession,
				'AuthorProfilePicture': translation.AuthorProfilePicture.url,
			})
		return Response(data)

	def list(self, request, *args, **kwargs):
		fArticles = {}
		if 'type' in request.query_params:
			fArticles['ArticleType_id'] = int(request.query_params['type'])

		fTranslations = {}
		fIngredients = {}
		if 'locale' in request.query_params:
			if (not request.user.is_superuser) or 'admin' not in request.query_params:
				fTranslations['Language_id'] = int(request.query_params['locale'])
				fIngredients['Language_id'] = int(request.query_params['locale'])

		if 'carousel' in request.query_params:
			fTranslations['OnCarousel'] = True

		if 'home' in request.query_params:
			fTranslations['OnCarousel'] = False

		articles = Article.objects.filter(**fArticles).all()

		data = []
		for article in articles:
			translation = article.articlecontenttranslation_set.filter(**fTranslations).first()
			if not translation:
				continue
			if not request.user.is_superuser and not translation.Released:
				continue
			translationData = {
				'id': article.id,
				'ArticleTypeId': article.ArticleType_id,
				'Title': translation.Title,
				'Preview': translation.Preview,
				'Thumbnail': translation.Thumbnail.url,
				'Dishes': translation.Dishes,
				'Cooking': translation.Cooking,
				'Preparation': translation.Preparation,
				'Waiting': translation.Waiting,
				'ReleaseDateTime': translation.ReleaseDateTime
			}

			if article.ArticleType_id == 1:
				ingredientList = IngredientAssociation.objects.filter(Article_id=article.id, IsMainIngredient=True).all()
				ingredients = []
				for ingredient in ingredientList:
					ingredientName = ingredient.Ingredient.Name
					if 'locale' in request.query_params:
						if ingredient.Ingredient.Language_id != int(request.query_params['locale']):
							ingredientName = ingredient.Ingredient.ingredientnametranslation_set.filter(**fIngredients).first().Name
					ingredients.append(ingredientName)
				translationData['MainIngredients'] = ', '.join(ingredients)
			data.append(translationData)
		data = sorted(data, key=lambda k: k['ReleaseDateTime'], reverse=True)
		return Response(data)

	def create(self, request, *args, **kwargs):
		at = request.data['articleType']
		a = Article(User=User.objects.filter(is_superuser=True).first(), ArticleType_id=at)
		a.save()
		translations = request.data['translations']
		ata = ArticleTypeAssociation(Article=a, Type_id=at)
		ata.save()
		for translation in translations:
			act = ArticleContentTranslation(Article=a, Language_id=translation['language'])
			act.Title = translation['title']
			act.Content = translation['content']
			act.Thumbnail = base64toFile(translation['thumbnail']['name'], translation['thumbnail']['data'])
			dateStr = translation['releaseDateTime']['date'] + '-' + translation['releaseDateTime']['time'] + '-' + 'UTC'
			act.ReleaseDateTime = datetime.strptime(dateStr, '%d/%m/%Y-%H:%M-%Z')
			act.DoneEditing = translation['doneEditing']
			if translation['preview'] == '':
				soup = BeautifulSoup(translation['content'], features='html.parser')
				rawText = soup.get_text()
				act.Preview = (rawText[:100] if len(rawText) > 100 else rawText) + '...'
			else:
				act.Preview = translation['preview']
			if at == 1:
				act.Dishes = request.data['dishes']
				act.Cooking = request.data['Cooking']
				act.Preparation = request.data['Preparation']
				act.Waiting = request.data['Waiting']
				act.YoutubeLink = request.data['youtubeLink']
			elif at == 2:
				act.AuthorName = translation['authorName']
				act.AuthorProfession = translation['authorProfession']
				act.AuthorProfilePicture = base64toFile(translation['authorProfilePicture']['name'], translation['authorProfilePicture']['data'])
			act.OnCarousel = translation['onCarousel']
			act.save()
		if at == 1:
			ingredients = request.data['ingredients']
			for ingredient in ingredients:
				ia = IngredientAssociation(Article=a, Ingredient_id=ingredient['ingredientId'], Quantity=ingredient['quantity'], IsMainIngredient=ingredient['isMainIngredient'])
				ia.save()
		return Response(status=HTTP_201_CREATED)

	def update(self, request, *args, **kwargs):
		at = request.data['ArticleTypeId']
		translations = request.data['Translations']
		for translation in translations:
			if translation['id'] == -1:
				act = ArticleContentTranslation(Article_id=kwargs['pk'])
			else:
				act = ArticleContentTranslation.objects.filter(id=translation['id']).first()
				if not act:
					continue
			act.Language_id = translation['Language']
			act.Title = translation['Title']
			if translation['Preview'] == '':
				soup = BeautifulSoup(translation['Content'], features='html.parser')
				rawText = soup.get_text()
				act.Preview = (rawText[:100] if len(rawText) > 100 else rawText) + '...'
			else:
				act.Preview = translation['Preview']
			act.Content = translation['Content']

			if 'name' in translation['Thumbnail'] and translation['Thumbnail']['name'] != '':
				act.Thumbnail = base64toFile(translation['Thumbnail']['name'], translation['Thumbnail']['data'])

			dateStr = translation['ReleaseDateTime']['date'] + '-' + translation['ReleaseDateTime']['time'] + '-' + 'UTC'
			act.ReleaseDateTime = datetime.strptime(dateStr, '%d/%m/%Y-%H:%M-%Z')
			act.DoneEditing = translation['DoneEditing']
			act.OnCarousel = translation['OnCarousel']

			if at == 1:
				act.Dishes = request.data['Dishes']
				act.Cooking = request.data['Cooking']
				act.Preparation = request.data['Preparation']
				act.Waiting = request.data['Waiting']
				act.YoutubeLink = request.data['YoutubeLink']
			if at == 2:
				act.AuthorName = translation['AuthorName']
				act.AuthorProfession = translation['AuthorProfession']
				if 'name' in translation['AuthorProfilePicture'] and translation['AuthorProfilePicture']['name']:
					act.AuthorProfilePicture = base64toFile(translation['AuthorProfilePicture']['name'], translation['AuthorProfilePicture']['data'])
			act.save()

		return Response(status=HTTP_200_OK)

	def destroy(self, request, *args, **kwargs):
		if 'locale' not in request.query_params:
			return super().destroy(request, *args, **kwargs)
		articleTranslation = ArticleContentTranslation.objects.get(Article_id=kwargs['pk'], Language_id=request.query_params['locale'])
		articleTranslation.delete()
		article = Article.objects.get(id=kwargs['pk'])
		if not article.articlecontenttranslation_set.count():
			article.delete()
		return Response(status=HTTP_200_OK)


class ArticleTypeViewSet(viewsets.ModelViewSet):
	queryset = ArticleType.objects.all()
	serializer_class = ArticleTypeSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class IngredientViewSet(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		queryset = Ingredient.objects.all()
		serializer = self.get_serializer(queryset, many=True)

		data = {}
		if 'locale' in request.query_params:
			locale = int(request.query_params['locale'])
			for obj in serializer.data:
				# objData = obj
				if obj['Language'] != locale:
					translation = IngredientNameTranslation.objects.filter(Ingredient_id=obj['id'], Language_id=locale).first()
					if not translation:
						continue
					obj['Name'] = translation.Name
				data[obj['id']] = obj
			return Response(data)

		for obj in serializer.data:
			objData = obj
			objData['translations'] = {2: ''}
			translations = IngredientNameTranslation.objects.filter(Ingredient_id=obj['id']).all()
			for translation in translations:
				objData['translations'][translation.Language.id] = translation.Name
			data[objData['id']] = objData
		return Response(data)

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
		if not kwargs['pk'].isdigit():
			return Response(status=HTTP_400_BAD_REQUEST)
		queryset = IngredientAssociation.objects.filter(Article_id=kwargs['pk']).order_by('-IsMainIngredient')
		serializer = self.get_serializer(queryset, many=True)
		data = serializer.data
		return Response(data)


class ArticleContentTranslationViewSet(viewsets.ModelViewSet):
	queryset = ArticleContentTranslation.objects.all()
	serializer_class = ArticleContentTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleTypeNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = ArticleTypeNameTranslation.objects.all()
	serializer_class = ArticleTypeNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleTypeAssociationViewSet(viewsets.ModelViewSet):
	queryset = ArticleTypeAssociation.objects.all()
	serializer_class = ArticleTypeAssociationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

# class TagViewSet(viewsets.ModelViewSet):
# 	queryset = Tag.objects.all()
# 	serializer_class = TagSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class TagNameTranslationViewSet(viewsets.ModelViewSet):
# 	queryset = TagNameTranslation.objects.all()
# 	serializer_class = TagNameTranslationSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class TagAssociationViewSet(viewsets.ModelViewSet):
# 	queryset = TagAssociation.objects.all()
# 	serializer_class = TagAssociationSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class UnitViewSet(viewsets.ModelViewSet):
# 	queryset = Unit.objects.all()
# 	serializer_class = UnitSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class UnitNameTranslationViewSet(viewsets.ModelViewSet):
# 	queryset = UnitNameTranslation.objects.all()
# 	serializer_class = UnitNameTranslationSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)
