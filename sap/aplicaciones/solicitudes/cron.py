__author__ = 'eduardo'
from django_cron import CronJobBase, Schedule
from .models import Solicitudes, Credenciales
from django.core.mail import send_mail
from datetime import timedelta
import datetime
from django.contrib.auth.models import User

class CronExpirador(CronJobBase):
    RUN_EVERY_MINS = 120
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
    code = 'solicitudes.CronExpirador'

    def do(self):
        print "2 min Cron"
        self.expiracionDeSolicitud()
        self.expiracionDeCredencial()
        self.pruebaDeFuncionamientoCron()

    def expiracionDeSolicitud(self):
        administradorSistema = User.objects.get(id=1)
        listaSolicitudesPendientes = Solicitudes.objects.filter(estado='Pendiente')
        for solicitud in listaSolicitudesPendientes:
            fechaExpiracion = solicitud.fecha_solicitud + timedelta(days=solicitud.tiempo_esperado)
            if fechaExpiracion == datetime.date.today():
                #Si la fecha de hoy es igual a la fecha de expiracion de la solicitud
                #entonces cambiamos el estado de la solicitud a expirada y enviamos un correo de Notificacion al usuario
                solicitud.estado = 'Cancelado'
                solicitud.save()
                send_mail(solicitud.usuario.user.username, 'Su solicitud ha experido sin respuestas por parte del miembro de comite, favor comunicarse con el lider del proyecto o realizar una nueva solicitud de cambio',
                          administradorSistema.email, [solicitud.usuario.user.email], fail_silently=False)
    def expiracionDeCredencial(self):
        administradorSistema = User.objects.get(id=1)
        listaCredencialesHabilitadas = Credenciales.objects.filter(estado='Habilitado')
        for credencial in listaCredencialesHabilitadas:
            if credencial.fecha_expiracion == datetime.date.today():
                #Si la fecha de hoy es igual a la fecha de expiracion de la credencial
                #entonces la credencial cambia al estado Revocado y el item habilitado
                #para el cambio vuelve a la version en la que estaba antes de generar la
                #credencial


                ### Ysa aca tenes que poner tu codigo que regresa al item a su 'version' anterior a la generacion de la credencial
                credencial.estado = 'Revocado'
                send_mail(credencial.usuario.user.username, 'Su credencial ha sido revocada debido a que si credencial expiro, favor comunicarse con el lider del proyecto o realizar una nueva solicitud de cambio',
                          administradorSistema.email, [credencial.usuario.user.email], fail_silently=False)


    def pruebaDeFuncionamientoCron(self):
        listaSolicitudesRechazadas = Solicitudes.objects.filter(estado='Pendiente')
        for solicitud in listaSolicitudesRechazadas:
            solicitud.estado = 'Reprobada'
            solicitud.save()