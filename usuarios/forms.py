from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['formacao', 'afiliacoes', 'especialidades', 'bio']
