import os
import sys
sys.path = ['/home/eduardo/workspace/is2_git/sap'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
