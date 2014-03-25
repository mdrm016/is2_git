import os
import sys
sys.path = ['/home/mdrm016/workspace/sap'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
