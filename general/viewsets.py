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

	def retrieve(self, request, *args, **kwargs):
		if 'locale' not in request.query_params:
			return super().retrieve(request, *args, **kwargs)
		locale = int(request.query_params['locale'])
		staticPage = StaticPage.objects.get(id=kwargs['pk'])
		translation = staticPage.staticpagetranslation_set.filter(Language_id=locale).first() if request.user.is_superuser else staticPage.staticpagetranslation_set.filter(Language_id=locale, Listed=True, Private=False).first()
		if translation:
			return Response(StaticPageTranslationSerializer(translation).data)
		return Response(status=HTTP_404_NOT_FOUND)

	def list(self, request, *args, **kwargs):
		staticPages = StaticPage.objects.all()
		res = {}
		for staticPage in staticPages:
			spts = staticPage.staticpagetranslation_set.all() if request.user.is_superuser else staticPage.staticpagetranslation_set.filter(Listed=True, Private=False).all()
			translations = {translation.Language_id: translation.id for translation in spts}
			if translations:
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

	def retrieve(self, request, *args, **kwargs):
		queryset = StaticPageTranslation.objects.filter(id=kwargs['pk']).first() if request.user.is_superuser else StaticPageTranslation.objects.filter(id=kwargs['pk'], Private=False).first()
		if queryset:
			serializer = self.get_serializer(queryset)
			return Response(serializer.data)
		return Response(status=HTTP_401_UNAUTHORIZED)

	def list(self, request, *args, **kwargs):
		queryset = StaticPageTranslation.objects.all() if request.user.is_superuser else StaticPageTranslation.objects.filter(Private=False).all()
		if queryset:
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)
		return Response(status=HTTP_401_UNAUTHORIZED)

	def create(self, request, *args, **kwargs):
		if request.data['id'] != -1:
			return Response(status=HTTP_406_NOT_ACCEPTABLE)

		staticPageId = request.data['StaticPage']
		sp = None
		if staticPageId == -1:
			sp = StaticPage()
			sp.save()
			staticPageId = sp.id

		spt = StaticPageTranslation(
			StaticPage_id=staticPageId,
			Language_id=request.data['Language'],
			Name=request.data['Name'],
			Content=request.data['Content'],
			Listed=request.data['Listed'],
			Private=request.data['Private']
		)
		spt.save()

		if sp:
			sp.Main = spt
			sp.save()
		return Response(status=HTTP_201_CREATED)

	def partial_update(self, request, *args, **kwargs):
		spt = StaticPageTranslation.objects.filter(id=request.data['id'])
		if not spt:
			return Response(status=HTTP_404_NOT_FOUND)
		spt.update(
			Language_id=request.data['Language'],
			Name=request.data['Name'],
			Content=request.data['Content'],
			Listed=request.data['Listed'],
			Private=request.data['Private']
		)
		return Response(status=HTTP_206_PARTIAL_CONTENT)

	def destroy(self, request, *args, **kwargs):
		spt = StaticPageTranslation.objects.get(id=kwargs['pk'])
		if not spt:
			return Response(status=HTTP_404_NOT_FOUND)
		sp = StaticPage.objects.get(id=spt.StaticPage_id)
		sp.Main = None
		sp.save()

		spt.delete()
		spts = sp.staticpagetranslation_set.first()
		if spts:
			sp.Main = spts
			sp.save()
		else:
			sp.delete()
		return Response(status=HTTP_200_OK)
