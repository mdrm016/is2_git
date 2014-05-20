import os
import sys
from unipath import Path

p = Path("/home/ysapy/workspace/is2_git/sap")
sys.path = [p] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.contrib.auth.management.commands import changepassword
from django.core import management

# Run the syncdb
management.call_command('syncdb', interactive=False)

# Create the super user and sets his password.
management.call_command('createsuperuser', interactive=False, username="sap", email="sap@sap.com")
command = changepassword.Command()
command._get_pass = lambda *args: 'sap'
command.execute("sap")
