from django import forms
from .models import Producto, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'categoria', 'marca']

class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ['nombre', 'valor']

CaracteristicaFormSet = forms.inlineformset_factory(
    Producto, Caracteristica, form=CaracteristicaForm, extra=1, can_delete=True
)