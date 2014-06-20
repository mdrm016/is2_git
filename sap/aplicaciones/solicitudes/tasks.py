from celery.task.schedules import crontab
from celery.decorators import periodic_task
from aplicaciones.solicitudes import expiraciones
from celery.utils.log import get_task_logger
from datetime import datetime


logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(hour=0, minute=0, day_of_week="*")))
def expiracionesSolicitudesCredenciales():
    logger.info("Inicio de la tarea de expiraciones")
    expiraciones.expiracionDeSolicitud()
    expiraciones.expiracionDeCredencial()
    logger.info("Tarea de solicitudes y credenciales expiradas terminada!!")