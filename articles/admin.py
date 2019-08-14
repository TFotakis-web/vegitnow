from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin

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
# class SummernoteAdmin(SummernoteModelAdmin):
# 	summernote_fields = '__all__'

class GeneralAdmin(admin.ModelAdmin):
	class Media:
		js = (
			'general/js/js.cookie.min.js',
		)


admin.site.register(Article)
admin.site.register(ArticleContentTranslation, GeneralAdmin)
admin.site.register(ArticleType)
admin.site.register(ArticleTypeNameTranslation)
admin.site.register(ArticleTypeAssociation)
admin.site.register(Ingredient)
admin.site.register(IngredientNameTranslation)
admin.site.register(IngredientAssociation)

# admin.site.register(Tag, SummernoteAdmin)
# admin.site.register(TagNameTranslation, SummernoteAdmin)
# admin.site.register(TagAssociation, SummernoteAdmin)
# admin.site.register(Unit, SummernoteAdmin)
# admin.site.register(UnitNameTranslation, SummernoteAdmin)
# admin.site.register(UnitAssociation, SummernoteAdmin)
