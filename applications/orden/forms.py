from django import forms
from .models import Pedido

class pedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['first_name', 'last_name','telefono', 'direccion','ciudad','provincia','codPostal']

    