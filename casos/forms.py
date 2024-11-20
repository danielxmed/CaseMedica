from django import forms
from .models import CasoClinico, Comentario

class CasoClinicoForm(forms.ModelForm):
    class Meta:
        model = CasoClinico
        fields = ['titulo', 'descricao', 'diagnostico', 'tratamento', 'conclusao', 'publicado', 'imagem', 'legenda_imagem']
        
    def clean_imagem(self):
        imagem = self.cleaned_data.get('imagem', False)
        if imagem:
            if imagem.size > 4 * 1024 * 1024:
                raise forms.ValidationError("A imagem não pode exceder 4MB.")
            if not imagem.content_type in ["image/jpeg", "image/png"]:
                raise forms.ValidationError("Formato de imagem não suportado. Use JPEG ou PNG.")
        return imagem

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3}),
        }
