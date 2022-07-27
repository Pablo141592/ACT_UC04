from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from miapp.models import Estudiantes

# Create your views here.

layout = """
<h1> Proyecto Web (LP3) | roxana  </h1>
<hr>
<ul>
        <li>
        <a href="/intregrantes"> Integrantes</a>
        </li>
        <li>
        <a href="/saludo"> Mensaje de saludo</a>
        </li>
        <li>
       
</ul>
</hr>
"""
def index(request):
    integrantes=['Roxana Condori Condori',                
                'Ricardo Pablo Trigo Suarez',
                'Fernando Acuña Saavedra',                
                ]
   

    return render(request,'index.html', {
        'titulo':'Integrantes',
        'integrantes':integrantes
    })
def saludo(request):
    
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        
    })

def guardar_estudiante(request):
    if request.method == 'GET':
        codigo = request.GET['codigo']
        dni = request.GET['dni']
        nombre = request.GET['nombre']
        apepat = request.GET['apepat']
        apemat = request.GET['apemat']
        direccion = request.GET['direccion']
        telefono = request.GET['telefono']
        estado = request.GET['estado']


        estudiante = Estudiantes(
            codigo = codigo,
            dni = dni,
            nombre = nombre,
            apepat= apepat,
            apemat= apemat,
            direccion= direccion,
            telefono= telefono,
            estado= estado,
        )
        estudiante.save()
        return HttpResponse(f"Estudiante Creado: {estudiante.codigo} - {estudiante.dni} - {estudiante.nombre} - {estudiante.apepat} - {estudiante.apemat} - {estudiante.direccion} - {estudiante.telefono} - {estudiante.estado}")
    else:
        return HttpResponse("<h2>No se ha podido registrar el artículo</h2>")

 
def crear_estudiante(request):
    return render(request, 'crear_estudiante.html')

