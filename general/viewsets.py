from datetime import datetime
from random import shuffle

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.viewsets import GenericViewSet

from articles.viewsets import base64toFile
from general.models import Ad, AdTranslation
from general.models import Language
from general.models import NewsletterUser
from general.models import StaticPage
from general.models import StaticPageTranslation
from general.serializers import AdSerializer
from general.serializers import LanguageSerializer
from general.serializers import NewsletterUserSerializer
from general.serializers import StaticPageSerializer
from general.serializers import StaticPageTranslationSerializer


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
	serializer_class = NewsletterUserSerializer


class AdViewSet(viewsets.ModelViewSet):
	queryset = Ad.objects.all()
	serializer_class = AdSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def list(self, request, *args, **kwargs):
		if 'id' in request.query_params:
			ad = Ad.objects.get(id=int(request.query_params['id']))
			ad.Clicks += 1
			ad.save()
			return Response(status=HTTP_200_OK)

		if request.user.is_superuser and 'admin' in request.query_params:
			ads = Ad.objects.all()
			resp = []
			for ad in ads:
				translations = []
				for translation in ad.adtranslation_set.all():
					translations.append({
						'id': translation.id,
						'Language': translation.Language.id,
						'Image': {
							'name': '',
							'data': ''
						},
						'Link': translation.Link,
					})
				resp.append({
					'id': ad.id,
					'Name': ad.Name,
					'AdType': ad.AdType,
					'Clicks': ad.Clicks,
					'TargetClicks': ad.TargetClicks,
					'ReleaseDateTime': {
						'date': ad.ReleaseDateTime.strftime('%d/%m/%Y'),
						'time': ad.ReleaseDateTime.strftime('%H:%M')
					},
					'RemoveDateTime': {
						'date': ad.RemoveDateTime.strftime('%d/%m/%Y'),
						'time': ad.RemoveDateTime.strftime('%H:%M')
					},
					'Translations': translations
				})
		else:
			f = {}
			if 'type' in request.query_params:
				f['AdType'] = request.query_params['type']

			ads = Ad.objects.filter(**f).all()
			resp = []
			f = {}
			if 'locale' in request.query_params:
				f['Language_id'] = int(request.query_params['locale'])
			for ad in ads:
				if not ad.Active:
				# if (not request.user.is_superuser) and not ad.Active:
					continue
				translation = ad.adtranslation_set.filter(**f).first()
				if not translation:
					continue
				resp.append({
					'id': ad.id,
					'Image': translation.Image.url,
					'Link': translation.Link,
				})
			shuffle(resp)
		return Response(resp)

	def create(self, request, *args, **kwargs):
		ad = Ad(
			Name=request.data['Name'],
			AdType=request.data['AdType'],
			TargetClicks=request.data['TargetClicks'],
			ReleaseDateTime=datetime.strptime(request.data['ReleaseDateTime']['date'] + '-' + request.data['ReleaseDateTime']['time'] + '-' + 'UTC', '%d/%m/%Y-%H:%M-%Z'),
			RemoveDateTime=datetime.strptime(request.data['RemoveDateTime']['date'] + '-' + request.data['RemoveDateTime']['time'] + '-' + 'UTC', '%d/%m/%Y-%H:%M-%Z'),
		)
		ad.save()
		for translation in request.data['Translations']:
			adTranslation = AdTranslation(
				Ad=ad,
				Language_id=translation['Language'],
				Image=base64toFile(translation['Image']['name'], translation['Image']['data']),
				Link=translation['Link']
			)
			adTranslation.save()
		return Response(status=HTTP_200_OK)

	def update(self, request, *args, **kwargs):
		try:
			ad = Ad.objects.get(id=kwargs['pk'])
		except:
			return Response(status=HTTP_404_NOT_FOUND)
		ad.Name = request.data['Name']
		ad.AdType = request.data['AdType']
		ad.TargetClicks = request.data['TargetClicks']
		ad.ReleaseDateTime = datetime.strptime(request.data['ReleaseDateTime']['date'] + '-' + request.data['ReleaseDateTime']['time'] + '-' + 'UTC', '%d/%m/%Y-%H:%M-%Z')
		ad.RemoveDateTime = datetime.strptime(request.data['RemoveDateTime']['date'] + '-' + request.data['RemoveDateTime']['time'] + '-' + 'UTC', '%d/%m/%Y-%H:%M-%Z')
		ad.save()

		for translation in request.data['Translations']:
			if translation['id'] == -1:
				adTranslation = AdTranslation()
			else:
				try:
					adTranslation = AdTranslation.objects.get(id=translation['id'])
				except:
					continue
			adTranslation.Ad = ad
			adTranslation.Language_id = translation['Language']
			if translation['Image']['data']:
				adTranslation.Image = base64toFile(translation['Image']['name'], translation['Image']['data'])
			adTranslation.Link = translation['Link']
			adTranslation.save()
		return Response(status=HTTP_200_OK)

	def destroy(self, request, *args, **kwargs):
		if 'translationId' not in request.query_params:
			return super().destroy(request)
		AdTranslation.objects.filter(id=request.query_params['translationId']).delete()
		return Response(status=HTTP_200_OK)
