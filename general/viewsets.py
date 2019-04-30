from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.viewsets import GenericViewSet

from .models import Language, StaticPage, StaticPageTranslation, NewsletterUser
from .serializers import LanguageSerializer, StaticPageSerializer, StaticPageTranslationSerializer, NewsletterUserSerializer


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
		if not kwargs['pk'].isdigit():
			return Response(status=HTTP_400_BAD_REQUEST)
		staticPage = StaticPage.objects.get(id=kwargs['pk'])
		f = {}
		if 'locale' in request.query_params:
			f['Language_id'] = int(request.query_params['locale'])
		if not request.user.is_superuser:
			f['Listed'] = True
			f['Private'] = False
		translation = staticPage.staticpagetranslation_set.filter(**f).first()
		if translation:
			return Response(StaticPageTranslationSerializer(translation).data)
		return Response(status=HTTP_404_NOT_FOUND)

	def list(self, request, *args, **kwargs):
		staticPages = StaticPage.objects.all()
		f = {}
		if not request.user.is_superuser:
			f['Listed'] = True
			f['Private'] = False

		if 'locale' in request.query_params:
			f['Language_id'] = int(request.query_params['locale'])

			res = []
			for staticPage in staticPages:
				translation = staticPage.staticpagetranslation_set.filter(**f).first()
				if translation:
					res.append({
						'id': staticPage.id,
						'Name': translation.Name
					})
			return Response(res)

		res = {}
		for staticPage in staticPages:
			spts = staticPage.staticpagetranslation_set.filter(**f).all()
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
		if not kwargs['pk'].isdigit():
			return Response(status=HTTP_400_BAD_REQUEST)
		f = {'id': kwargs['pk']}
		if not request.user.is_superuser:
			f['Private'] = False
		queryset = StaticPageTranslation.objects.filter(**f).first()
		if queryset:
			serializer = self.get_serializer(queryset)
			return Response(serializer.data)
		return Response(status=HTTP_401_UNAUTHORIZED)

	def list(self, request, *args, **kwargs):
		f = {}
		if not request.user.is_superuser:
			f['Private'] = False
		queryset = StaticPageTranslation.objects.filter(**f).all()
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

	def update(self, request, *args, **kwargs):
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


class NewsletterUserViewSet(viewsets.ModelViewSet):
	queryset = NewsletterUser.objects.all()
	serializer_class = NewsletterUserSerializer
	permission_classes = (IsAdminUser,)


class CreateNewsletterUserViewSet(mixins.CreateModelMixin, GenericViewSet):
	# queryset = NewsletterUser.objects.all()
	serializer_class = NewsletterUserSerializer
	# permission_classes = (IsAdminUser,)
