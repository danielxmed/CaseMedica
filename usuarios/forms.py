from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from PIL import Image

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['formacao', 'afiliacoes', 'especialidades', 'bio', 'imagem_perfil']

    def clean_imagem_perfil(self):
        imagem = self.cleaned_data.get('imagem_perfil', False)
        if imagem:
            if imagem.size > 4 * 1024 * 1024:
                raise forms.ValidationError("A imagem não pode exceder 4MB.")
            if not imagem.content_type in ["image/jpeg", "image/png"]:
                raise forms.ValidationError("Formato de imagem não suportado. Use JPEG ou PNG.")
        return imagem
    
    def save(self, commit=True):
        perfil = super().save(commit=False)
        if commit:
            perfil.save()
            if perfil.imagem_perfil:
                imagem = Image.open(perfil.imagem_perfil.path)
                if imagem.height > 300 or imagem.width > 300:
                    output_size = (300, 300)
                    imagem.thumbnail(output_size)
                    imagem.save(perfil.imagem_perfil.path)
        return perfil
