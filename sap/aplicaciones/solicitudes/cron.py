__author__ = 'eduardo'
from django_cron import CronJobBase, Schedule
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 240
    RUN_AT_TIMES = ['6:30']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
