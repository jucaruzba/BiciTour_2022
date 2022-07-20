
from django import forms

from .models import ComentarioUsuario


class ComentarioUserForm(forms.ModelForm):
    class Meta:
        model = ComentarioUsuario
        fields = ['nombre','email', 'mensaje']