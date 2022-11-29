from django import forms


class alumnoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    expte = forms.IntegerField()

class profesoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    numero = forms.IntegerField()
    
class preceptorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()