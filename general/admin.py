from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Language, StaticPage, StaticPageTranslation, NewsletterUser, Ad, AdTranslation


# Apply summernote to all TextField in model.
class SummernoteAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


admin.site.register(Language)
admin.site.register(StaticPage, SummernoteAdmin)
admin.site.register(StaticPageTranslation, SummernoteAdmin)
admin.site.register(NewsletterUser, SummernoteAdmin)
admin.site.register(Ad, SummernoteAdmin)
admin.site.register(AdTranslation, SummernoteAdmin)
