from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from .models import Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation, Ingredient, IngredientNameTranslation, IngredientAssociation, Unit, UnitNameTranslation#, UnitAssociation
from .serializers import ArticleSerializer, ArticleContentTranslationSerializer, ArticleTypeSerializer, ArticleTypeNameTranslationSerializer, ArticleTypeAssociationSerializer, TagSerializer, TagNameTranslationSerializer, TagAssociationSerializer, IngredientSerializer, IngredientNameTranslationSerializer, IngredientAssociationSerializer, UnitSerializer, UnitNameTranslationSerializer#, UnitAssociationSerializer


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


class IngredientNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = IngredientNameTranslation.objects.all()
	serializer_class = IngredientNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class IngredientAssociationViewSet(viewsets.ModelViewSet):
	queryset = IngredientAssociation.objects.all()
	serializer_class = IngredientAssociationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class UnitViewSet(viewsets.ModelViewSet):
	queryset = Unit.objects.all()
	serializer_class = UnitSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class UnitNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = UnitNameTranslation.objects.all()
	serializer_class = UnitNameTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


# class UnitAssociationViewSet(viewsets.ModelViewSet):
# 	queryset = UnitAssociation.objects.all()
# 	serializer_class = UnitAssociationSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)


class NewArticleViewSet(viewsets.ViewSet):
	permission_classes = (IsAdminUser,)
	SAFE_ACTIONS = ['list', 'retrieve', 'create']

	def list(self, request):
		print('List')
		return Response()

	def create(self, request):
		print('Create')
		a = Article(User=User.objects.filter(is_superuser=True).first())
		a.save()
		at = request.data['articleType']
		translations = request.data['translations']

		print(at)
		print(translations)
		ata = ArticleTypeAssociation(Article=a, Type_id=at)
		ata.save()
		for translation in translations:
			ac = ArticleContentTranslation(Article=a, Language_id=translation['language'])
			ac.Title = translation['title']
			ac.Content = translation['content']
			ac.Thumbnail = translation['thumbnail']
			dateStr = translation['releaseDateTime']['date'] + '-' + translation['releaseDateTime']['time'] + '-' + 'UTC'
			ac.ReleaseDateTime = datetime.strptime(dateStr, '%d/%m/%Y-%H:%M-%Z')
			ac.DoneEditing = translation['doneEditing']
			ac.save()
		if at == 1:
			ingredients = request.data['ingredients']
			for ingredient in ingredients:
				ia = IngredientAssociation(Article=a, Ingredient_id=ingredient['ingredient']['id'], Quantity=ingredient['quantity'], IsMainIngredient=ingredient['isMainIngredient'])
				ia.save()

		return Response()

	def retrieve(self, request, pk=None):
		print('Retrieve')
		return Response()

	def update(self, request, pk=None):
		print('Update')
		return Response()

	def partial_update(self, request, pk=None):
		print('Patch')
		return Response()

	def destroy(self, request, pk=None):
		print('Delete')
		return Response()
