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
		staticPages = StaticPage.objects.all()
		res = {}
		for staticPage in staticPages:
			translations = {translation.Language_id: translation.id for translation in staticPage.staticpagetranslation_set.all()}
			res[staticPage.id] = {
				'id': staticPage.id,
				'Name': staticPage.Main.Name,
				'data': [],
				'fetched': False,
				'translations': translations
			}
		return Response(res)


class StaticPageTranslationViewSet(viewsets.ModelViewSet):
	queryset = StaticPageTranslation.objects.all()
	serializer_class = StaticPageTranslationSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
