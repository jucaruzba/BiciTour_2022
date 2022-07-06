from typing import Sequence
from django.contrib import admin

from registros.models import Tours


class AdministrarTour(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    


admin.site.register(Tours, AdministrarTour)