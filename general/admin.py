from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin

from .models import Language, StaticPage, StaticPageTranslation, NewsletterUser, Ad, AdTranslation


# Apply summernote to all TextField in model.
# class SummernoteAdmin(SummernoteModelAdmin):
# 	summernote_fields = '__all__'

class GeneralAdmin(admin.ModelAdmin):
	class Media:
		js = (
			'general/js/js.cookie.min.js',
		)


admin.site.register(Language)
admin.site.register(StaticPage)
admin.site.register(StaticPageTranslation, GeneralAdmin)
admin.site.register(NewsletterUser)
admin.site.register(Ad)
admin.site.register(AdTranslation)
