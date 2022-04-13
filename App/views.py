from django.shortcuts import render
from django.http import HttpResponse
from App.models import Profesor, Trabajos, Familiares
from App.form import *

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def familia(request):
    families = Familiares.objects.all() # para vista lsita

    if request.method == 'POST':
        form = FormularioFamilia(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            family = Familiares(nombre=info['nombre'],apellido=info['apellido'],FechaDeNacimiento=info['FechaDeNacimiento'],dni=info['dni'],edad=info['edad'])
            family.save()
            return render(request,'confirmed/confirmagregado.html')
    else:
        family = FormularioFamilia()
    return render(request,'familiar.html', {'families':family,'vista':families})


def trabajo(request):
    work = Trabajos.objects.all() # para vista lsita
    if request.method == 'POST':
        form = Formulariojobs(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            jobs = Trabajos(nombre_empresa=info['nombre_form'],apellido_empresa=info['apellido_form'],email_empresa=info['email_form'],dni_empresa=info['dni_form'],telefono_empresa=info['telefono_form'],profesion_empresa=info['profesion_form'])
            jobs.save()
            return render(request,'confirmed2/confirmagregado.html')
    else:
        jobs = Formulariojobs() #vacio
    return render(request,'trabajos.html', {'jobs':jobs,'vista':work})
    

#Terminado
def master(request):
    
    profesor = Profesor.objects.all() # para vista lsita
    
    if request.method == 'POST':

        form = FormularioProfesion(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            master = Profesor(nombre_master=info['nombre_form'],apellido_master=info['apellido_form'],email_master=info['email_form'],dni_master=info['dni_form'],telefono_master=info['telefono_form'],profesion_master=info['profesion_form'])

            master.save()

            return render(request,'confirmed3/confirmagregado.html') #corre entrada
    else:

        master = FormularioProfesion() #vacio

    return render(request, 'profesion.html', {'fm2':master, 'vista':profesor})

def busqueda(request):
    return render(request, 'buscar.html')

#funciona bien eliminado para profesores
def borrar(request,name2):
    delmaster = Profesor.objects.filter(nombre_master=name2)
    delmaster.delete()
    delmaster = Profesor.objects.all()
    return render(request, 'confirmed3/confirmdelete.html',{"vista":delmaster})
#funciona bien 2
def borrar2(request,name4):
    delmaster = Trabajos.objects.filter(nombre_empresa=name4)
    delmaster.delete()
    delmaster = Trabajos.objects.all()
    return render(request, 'confirmed2/confirmdelete.html',{"vista":delmaster})
#funciona bien XD
def borrar3(request,name5):
    delmaster = Familiares.objects.filter(nombre=name5)
    delmaster.delete()
    delmaster = Familiares.objects.all()
    return render(request, 'confirmed/confirmdelete.html',{"vista":delmaster})



#solucionado XD
def search(request):
    if request.GET["nombre"]:
        ape = request.GET["nombre"]
        fm = Familiares.objects.filter(nombre=ape)
        return render(request, "result.html",{'fm':fm,'ape':ape})
    else:
        respuesta = 'no enviaste datos'
    return HttpResponse(respuesta)




#nada :(
def editarProfesor(request,name3):
    # editprofesor = Profesor.objects.(nombre_master=name3)
    editprofesor = Profesor.objects.get(nombre_master=name3)

    if request.method == 'POST':

        form = FormularioProfesion(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            editprofesor.nombre_master = info['nombre_form']
            editprofesor.apellido_master = info['apellido_form']
            editprofesor.email_master = info['email_form']
            editprofesor.dni_master = info['dni_form']
            editprofesor.telefono_master = info['telefono_form']
            editprofesor.profesion_master = info['profesion_form']


            editprofesor.save()
            return render(request,'confirmeditar.html')
    else:
        master = FormularioProfesion(initial={
            'nombre_form':editprofesor.nombre_master,
            'apellido_form':editprofesor.apellido_master,
            'email_form':editprofesor.email_master,
            'dni_form':editprofesor.dni_master,
            'telefono_form':editprofesor.telefono_master,
            'profesion_form':editprofesor.profesion_master
            })
    return render(request,'profesion.html', {'fm2':master, 'vista':name3})
