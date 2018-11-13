from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation


# Apply summernote to all TextField in model.
class SummernoteAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


# admin.site.register([Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation])

admin.site.register(Article, SummernoteAdmin)
admin.site.register(ArticleContentTranslation, SummernoteAdmin)
admin.site.register(ArticleType, SummernoteAdmin)
admin.site.register(ArticleTypeNameTranslation, SummernoteAdmin)
admin.site.register(ArticleTypeAssociation, SummernoteAdmin)
admin.site.register(Tag, SummernoteAdmin)
admin.site.register(TagNameTranslation, SummernoteAdmin)
admin.site.register(TagAssociation, SummernoteAdmin)
