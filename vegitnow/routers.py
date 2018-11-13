from rest_framework import routers

from articles.viewsets import ArticleViewSet, ArticleContentTranslationViewSet, ArticleTypeViewSet, ArticleTypeNameTranslationViewSet, ArticleTypeAssociationViewSet, TagViewSet, TagNameTranslationViewSet, TagAssociationViewSet
from general.viewsets import LanguageViewSet

router = routers.DefaultRouter()

router.register(r'language', LanguageViewSet)

router.register(r'article', ArticleViewSet)
router.register(r'articleContentTranslation', ArticleContentTranslationViewSet)
router.register(r'articleType', ArticleTypeViewSet)
router.register(r'articleTypeNameTranslation', ArticleTypeNameTranslationViewSet)
router.register(r'articleTypeAssociation', ArticleTypeAssociationViewSet)
router.register(r'tag', TagViewSet)
router.register(r'tagNameTranslation', TagNameTranslationViewSet)
router.register(r'tagAssociation', TagAssociationViewSet)
