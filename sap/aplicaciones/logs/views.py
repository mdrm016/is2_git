from django.shortcuts import render, render_to_response
from django.template import RequestContext
import os
from unipath import Path
from datetime import datetime, timedelta


# Create your views here.
directorioLog = Path(__file__).ancestor(3) + '/static/logs/'

def logHoy(request):
    hoy = []
    fechaHoy  = datetime.now()
    dia = str(fechaHoy.day)
    mes = str(fechaHoy.month)
    if len(mes) ==1:
        mes = "0"+mes
    anho = str(fechaHoy.year)
    fechaHoy = dia+"/"+mes+"/"+anho
    for nombreLog in os.listdir (directorioLog):
        ficheroActual = directorioLog + nombreLog
        with open(ficheroActual) as archivoLog:
            archivoLog = archivoLog.readlines()

        for linea in archivoLog:
                if fechaHoy in linea:
                    hoy.append(linea)
    template_name = 'Logs/log_hoy.html'
    ctx ={ 'hoy' : hoy}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def logAyer(request):
    ayer = []
    fechaAyer  = datetime.now() + timedelta(days=-1)
    dia = str(fechaAyer.day)
    mes = str(fechaAyer.month)
    if len(mes) ==1:
        mes = "0"+mes
    anho = str(fechaAyer.year)
    fechaAyer = dia+"/"+mes+"/"+anho
    for nombreLog in os.listdir (directorioLog):
        ficheroActual = directorioLog + nombreLog
        with open(ficheroActual) as archivoLog:
            archivoLog = archivoLog.readlines()

        for linea in archivoLog:
                if fechaAyer in linea:
                    ayer.append(linea)
    template_name = 'Logs/log_hoy.html'
    ctx ={ 'hoy' : ayer}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def logSemana1(request):
    unaSemana = []
    fechaUnaSemana  = datetime.now() + timedelta(days=-7)
    dia = str(fechaUnaSemana.day)
    mes = str(fechaUnaSemana.month)
    if len(mes) ==1:
        mes = "0"+mes
    anho = str(fechaUnaSemana.year)
    fechaUnaSemana = dia+"/"+mes+"/"+anho
    control = False
    for nombreLog in os.listdir (directorioLog):
        ficheroActual = directorioLog + nombreLog
        with open(ficheroActual) as archivoLog:
            archivoLog = archivoLog.readlines()

        for linea in archivoLog:
            if control:
                unaSemana.append(linea)
            if not control:
                if fechaUnaSemana in linea:
                    control = True
                    unaSemana.append(linea)
    template_name = 'Logs/log_hoy.html'
    ctx ={ 'hoy' : unaSemana}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def logSemana2(request):
    dosSemanas = []
    fechaDosSemanas  = datetime.now() + timedelta(days=-14)
    dia = str(fechaDosSemanas.day)
    mes = str(fechaDosSemanas.month)
    if len(mes) ==1:
        mes = "0"+mes
    anho = str(fechaDosSemanas.year)
    fechaDosSemanas = dia+"/"+mes+"/"+anho
    control = False
    for nombreLog in os.listdir (directorioLog):
        ficheroActual = directorioLog + nombreLog
        with open(ficheroActual) as archivoLog:
            archivoLog = archivoLog.readlines()

        for linea in archivoLog:
            if control:
                dosSemanas.append(linea)
            if not control:
                if fechaDosSemanas in linea:
                    control = True
                    dosSemanas.append(linea)
    template_name = 'Logs/log_hoy.html'
    ctx ={ 'hoy' : dosSemanas}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def logMas(request):
    masSemanas = []
    fechaMasSemanas  = datetime.now() + timedelta(days=-15)
    dia = str(fechaMasSemanas.day)
    mes = str(fechaMasSemanas.month)
    if len(mes) ==1:
        mes = "0"+mes
    anho = str(fechaMasSemanas.year)
    fechaMasSemanas = dia+"/"+mes+"/"+anho
    control = True
    for nombreLog in os.listdir (directorioLog):
        ficheroActual = directorioLog + nombreLog
        with open(ficheroActual) as archivoLog:
            archivoLog = archivoLog.readlines()

        for linea in archivoLog:
            if control:
                masSemanas.append(linea)
            if fechaMasSemanas in linea:
                control = False
                masSemanas.append(linea)
    template_name = 'Logs/log_hoy.html'
    ctx ={ 'hoy' : masSemanas}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
