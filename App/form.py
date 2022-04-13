from django import forms

class FormularioProfesion(forms.Form):
    nombre_form = forms.CharField(max_length=30)
    apellido_form = forms.CharField(max_length=30)
    email_form = forms.EmailField()
    dni_form = forms.IntegerField()
    telefono_form = forms.IntegerField()
    profesion_form = forms.CharField(max_length=30)

class Formulariojobs(forms.Form):
    nombre_form = forms.CharField(max_length=30)
    apellido_form = forms.CharField(max_length=30)
    email_form = forms.EmailField()
    dni_form = forms.IntegerField()
    telefono_form = forms.IntegerField()
    profesion_form = forms.CharField(max_length=30)


class FormularioFamilia(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    FechaDeNacimiento =forms.DateField(label="fecha",widget=forms.SelectDateWidget(years=range(1900,2001)))
    dni = forms.IntegerField()
    edad = forms.IntegerField()


