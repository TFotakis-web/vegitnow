from rest_framework import viewsets

from .models import Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation
from .serializers import ArticleSerializer, ArticleContentTranslationSerializer, ArticleTypeSerializer, ArticleTypeNameTranslationSerializer, ArticleTypeAssociationSerializer, TagSerializer, TagNameTranslationSerializer, TagAssociationSerializer


class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class ArticleContentTranslationViewSet(viewsets.ModelViewSet):
	queryset = ArticleContentTranslation.objects.all()
	serializer_class = ArticleContentTranslationSerializer


class ArticleTypeViewSet(viewsets.ModelViewSet):
	queryset = ArticleType.objects.all()
	serializer_class = ArticleTypeSerializer


class ArticleTypeNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = ArticleTypeNameTranslation.objects.all()
	serializer_class = ArticleTypeNameTranslationSerializer


class ArticleTypeAssociationViewSet(viewsets.ModelViewSet):
	queryset = ArticleTypeAssociation.objects.all()
	serializer_class = ArticleTypeAssociationSerializer


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


class TagNameTranslationViewSet(viewsets.ModelViewSet):
	queryset = TagNameTranslation.objects.all()
	serializer_class = TagNameTranslationSerializer


class TagAssociationViewSet(viewsets.ModelViewSet):
	queryset = TagAssociation.objects.all()
	serializer_class = TagAssociationSerializer
