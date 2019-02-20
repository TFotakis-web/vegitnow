from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Language, StaticPage, StaticPageTranslation


# Apply summernote to all TextField in model.
class SummernoteAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


admin.site.register(Language)
admin.site.register(StaticPage, SummernoteAdmin)
admin.site.register(StaticPageTranslation, SummernoteAdmin)
