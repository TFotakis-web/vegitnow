from rest_framework import routers

from articles.viewsets import ArticleTypeViewSet
from articles.viewsets import ArticleViewSet
from articles.viewsets import IngredientAssociationViewSet
from articles.viewsets import IngredientViewSet
from articles.viewsets import ArticleContentTranslationViewSet
# from articles.viewsets import ArticleTypeNameTranslationViewSet
# from articles.viewsets import ArticleTypeAssociationViewSet
# from articles.viewsets import IngredientNameTranslationViewSet
# from articles.viewsets import TagViewSet
# from articles.viewsets import TagNameTranslationViewSet
# from articles.viewsets import TagAssociationViewSet
# from articles.viewsets import UnitViewSet
# from articles.viewsets import UnitNameTranslationViewSet
from general.viewsets import LanguageViewSet, CreateNewsletterUserViewSet
from general.viewsets import NewsletterUserViewSet
from general.viewsets import StaticPageTranslationViewSet
from general.viewsets import StaticPageViewSet

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
# router.register(r'articleTypeNameTranslation', ArticleTypeNameTranslationViewSet)
# router.register(r'articleTypeAssociation', ArticleTypeAssociationViewSet)
# router.register(r'ingredientNameTranslation', IngredientNameTranslationViewSet)
# router.register(r'tag', TagViewSet)
# router.register(r'tagNameTranslation', TagNameTranslationViewSet)
# router.register(r'tagAssociation', TagAssociationViewSet)
# router.register(r'unit', UnitViewSet)
# router.register(r'unitNameTranslation', UnitNameTranslationViewSet)
