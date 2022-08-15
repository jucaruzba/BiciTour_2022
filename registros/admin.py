from django.contrib import admin
from .models import Archivos, ComentarioUsuario

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('nombre', 'mensaje', 'email')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    def get_readonly_fields(self, request, obj=None):
    #si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
    #Bloquea los campos
            return ('nombre','mensaje', 'email')
    #Cualquier otro usuario que no pertenece al grupo "Usuario"
        else:
    #Bloquea los campos
            return ('created', 'updated')

admin.site.register(ComentarioUsuario, AdministrarComentarios)

class AdmistrarArchivo(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'archivo')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    
    def get_readonly_fields(self, request, obj=None):
    #si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
    #Bloquea los campos
            return ('nombre','email', 'archivo')
    #Cualquier otro usuario que no pertenece al grupo "Usuario"
        else:
    #Bloquea los campos
            return ('created', 'updated')
    
    
admin.site.register(Archivos, AdmistrarArchivo)