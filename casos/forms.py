from django import forms
from .models import CasoClinico, Comentario

class CasoClinicoForm(forms.ModelForm):
    class Meta:
        model = CasoClinico
        fields = ['titulo', 'descricao', 'diagnostico', 'tratamento', 'conclusao', 'publicado']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3}),
        }
