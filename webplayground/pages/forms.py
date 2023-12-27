from django import forms
from .models import Page

class CrearPagina(forms.ModelForm):
      class Meta:
        model = Page
        fields = ['title', 'content', 'order']