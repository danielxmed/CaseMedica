from django import forms
from .models import CasoClinico

class CasoClinicoForm(forms.ModelForm):
    class Meta:
        model = CasoClinico
        fields = ['titulo', 'descricao', 'diagnostico', 'tratamento', 'conclusao', 'publicado']
