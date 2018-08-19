from django.contrib import admin

from .models import Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation

admin.site.register([Article, ArticleContentTranslation, ArticleType, ArticleTypeNameTranslation, ArticleTypeAssociation, Tag, TagNameTranslation, TagAssociation])
