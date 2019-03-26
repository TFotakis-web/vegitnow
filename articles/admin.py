from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from articles.models import Article
from articles.models import ArticleContentTranslation
from articles.models import ArticleType
from articles.models import ArticleTypeAssociation
from articles.models import ArticleTypeNameTranslation
from articles.models import Ingredient
from articles.models import IngredientAssociation
from articles.models import IngredientNameTranslation


# from articles.models import Tag
# from articles.models import TagNameTranslation
# from articles.models import TagAssociation
# from articles.models import Unit
# from articles.models import UnitNameTranslation
# from articles.models import UnitAssociation


# Apply summernote to all TextField in model.
class SummernoteAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


admin.site.register(Article, SummernoteAdmin)
admin.site.register(ArticleContentTranslation, SummernoteAdmin)
admin.site.register(ArticleType, SummernoteAdmin)
admin.site.register(ArticleTypeNameTranslation, SummernoteAdmin)
admin.site.register(ArticleTypeAssociation, SummernoteAdmin)
admin.site.register(Ingredient, SummernoteAdmin)
admin.site.register(IngredientNameTranslation, SummernoteAdmin)
admin.site.register(IngredientAssociation, SummernoteAdmin)
# admin.site.register(Tag, SummernoteAdmin)
# admin.site.register(TagNameTranslation, SummernoteAdmin)
# admin.site.register(TagAssociation, SummernoteAdmin)
# admin.site.register(Unit, SummernoteAdmin)
# admin.site.register(UnitNameTranslation, SummernoteAdmin)
# admin.site.register(UnitAssociation, SummernoteAdmin)
