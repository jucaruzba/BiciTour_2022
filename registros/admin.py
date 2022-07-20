from django.contrib import admin
from .models import ComentarioUsuario

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('nombre', 'mensaje', 'email')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioUsuario, AdministrarComentarios)