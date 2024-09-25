from django import forms

class VecinoFormulario(forms.Form):

    vecino =forms.CharField()
    domicilio = forms.CharField()

class ProvedorFormulario(forms.Form):

    provedor =forms.CharField()
    servicio = forms.CharField()
    precio_base = forms.FloatField()