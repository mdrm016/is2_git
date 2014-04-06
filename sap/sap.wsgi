import os
import sys
from unipath import Path
p=Path()
sys.path = [p.parent] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
