from rest_framework import routers

from articles.viewsets import ArticleViewSet, ArticleContentTranslationViewSet, ArticleTypeViewSet, ArticleTypeNameTranslationViewSet, ArticleTypeAssociationViewSet, TagViewSet, TagNameTranslationViewSet, TagAssociationViewSet, NewArticleViewSet, IngredientViewSet, IngredientNameTranslationViewSet, IngredientAssociationViewSet, UnitViewSet, UnitNameTranslationViewSet, NewIngredientViewSet
from general.viewsets import LanguageViewSet, StaticPageViewSet, StaticPageTranslationViewSet

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
router.register(r'ingredient', IngredientViewSet)
router.register(r'ingredientNameTranslation', IngredientNameTranslationViewSet)
router.register(r'ingredientAssociation', IngredientAssociationViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'unitNameTranslation', UnitNameTranslationViewSet)
router.register(r'newArticle', NewArticleViewSet, basename='newArticle')
router.register(r'newIngredient', NewIngredientViewSet, basename='newIngredient')
router.register(r'staticPage', StaticPageViewSet, basename='staticPage')
router.register(r'staticPageTranslation', StaticPageTranslationViewSet, basename='staticPageTranslation')
