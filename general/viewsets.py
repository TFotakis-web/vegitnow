from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import *

from .models import Language, StaticPage, StaticPageTranslation
from .serializers import LanguageSerializer, StaticPageSerializer, StaticPageTranslationSerializer


class LanguageViewSet(viewsets.ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		queryset = Language.objects.all()
		serializer = self.get_serializer(queryset, many=True)
		languages = {}
		for obj in serializer.data:
			languages[obj['id']] = obj
		return Response(languages)


class StaticPageViewSet(viewsets.ModelViewSet):
	queryset = StaticPage.objects.all()
	serializer_class = StaticPageSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		queryset = StaticPage.objects.all()
		serializer = self.get_serializer(queryset, many=True)
		staticPages = serializer.data

		queryset = StaticPageTranslation.objects.all()
		serializer = self.get_serializer(queryset, many=True)
		staticPagesTranslations = serializer.data

		data = {}
		for lang in Language.objects.all():
			data[lang.id] = {}
			for obj in staticPages:
				if obj['Language'] == lang.id:
					data[lang.id][obj['id']] = {
						'Name': obj['Name'],
						'IsNonTranslated': True
					}
			for obj in staticPagesTranslations:
				if obj['Language'] == lang.id:
					data[lang.id][obj['id']] = {
						'Name': obj['Name'],
						'IsNonTranslated': False
					}
		return Response(data)


class StaticPageTranslationViewSet(viewsets.ModelViewSet):
	queryset = StaticPageTranslation.objects.all()
	serializer_class = StaticPageTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
