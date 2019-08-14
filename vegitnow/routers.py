from rest_framework import routers

from articles.viewsets import ArticleTypeViewSet
from articles.viewsets import ArticleViewSet
from articles.viewsets import IngredientAssociationViewSet
from articles.viewsets import IngredientViewSet
from articles.viewsets import ArticleContentTranslationViewSet
from general.viewsets import LanguageViewSet
from general.viewsets import CreateNewsletterUserViewSet
from general.viewsets import NewsletterUserViewSet
from general.viewsets import StaticPageTranslationViewSet
from general.viewsets import StaticPageViewSet
from general.viewsets import AdViewSet
from general.viewsets import MediaViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'articleType', ArticleTypeViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'staticPage', StaticPageViewSet)
router.register(r'staticPageTranslation', StaticPageTranslationViewSet)
router.register(r'newsletterUser', NewsletterUserViewSet)
router.register(r'createNewsletterUser', CreateNewsletterUserViewSet, basename='createNewsletterUser')
router.register(r'ingredientAssociation', IngredientAssociationViewSet)
router.register(r'articleContentTranslation', ArticleContentTranslationViewSet)
router.register(r'vegitnowad', AdViewSet)
router.register(r'media', MediaViewSet, basename='media')
