from django.contrib import admin
from .models import *

class AllegatiInline(admin.StackedInline):
    model = Allegato
    extra = 1

class DettaglioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['descrizione_dettaglio', 'data_dettaglio', 'fase_dettaglio', 'lavoro_dettaglio']})
    ]
    inlines = [AllegatiInline, ]

admin.site.register(Categoria)
admin.site.register(Fase)
admin.site.register(Lavoro)
admin.site.register(Dettaglio, DettaglioAdmin)
