from django.contrib import admin
from models import Page,Block
from django.utils.translation import ugettext_lazy as _
# from forms import FlatpageForm
#
# class FlatPageAdmin(admin.ModelAdmin):
#     form = FlatpageForm
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites','in_menu',"use_gallerys")}),
#         (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
#     )
#     filter_horizontal = ("use_gallerys" ,)
#     list_display = ('url', 'title')
#     list_filter = ('sites', 'enable_comments', 'registration_required')
#     search_fields = ('url', 'title')
# class TextBlockAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Page)
admin.site.register(Block)
