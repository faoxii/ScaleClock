from django.contrib import admin
from django.db.models import Case, Value, When


# Register your models here.
from .models import Mode

class ModeAdmin(admin.ModelAdmin):
    list_display = ('tonality', 'mode_name')
    list_filter = ('tonality', 'mode_name')

    def get_ordering(self, request):
        # Définir l'ordre personnalisé
        custom_order = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A','A#','Bb', 'B']
        ordering = Case(*[When(tonality=value, then=pos) for pos, value in enumerate(custom_order, start=1)])
        return [ordering, 'mode_name']

admin.site.register(Mode, ModeAdmin)

