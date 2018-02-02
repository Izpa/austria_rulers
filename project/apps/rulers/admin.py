from django.contrib import admin

from project.apps.rulers.models import Ruler, RulerRequest


@admin.register(Ruler)
class RulerAdmin(admin.ModelAdmin):
    list_display = ('name', 'succession_order',)


@admin.register(RulerRequest)
class RulerRequestAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime', 'ruler', 'ruler_successors')
    list_display = ('datetime', 'ruler',)
