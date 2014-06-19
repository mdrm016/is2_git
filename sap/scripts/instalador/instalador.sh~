#!/bin/bash

#variables
#ruta de instalacion
rutainstalacion="/home/mdrm016/is2_git/is2_git"
#nombre del superusuario a crear en la BD
usuario='mdrm016'
#password del super usuario a crear en la BD
password='444444666666'
#ruta actual del instalador
rutainstalador=`pwd`
#localizacion de las iteraciones del codigo fuente del proyecto
iteracion1="https://github.com/mdrm016/is2_git/archive/Iteracion1.zip"
iteracion2="https://github.com/mdrm016/is2_git/archive/tag-iteracion2.zip"
iteracion3="https://github.com/mdrm016/is2_git/archive/iteracion3.zip"
iteracion4="https://github.com/mdrm016/is2_git/archive/iteracion4.zip"
iteracion5="https://github.com/mdrm016/is2_git/archive/iteracion5.zip"
iteracion6="https://github.com/mdrm016/is2_git/archive/iteracion6.zip"
actual="https://github.com/mdrm016/is2_git/archive/master.zip"

clear
echo "###### INICIANDO LA INSTALACION DEL SISTEMA DE ADMINISTRACION DE PROYECTOS (SAP) ######"
function iteracion
{
	echo 'Seleccione la iteracion que desea instalar:'
	echo ' 1 Iteracion1'
	echo ' 2 Iteracion2'
	echo ' 3 Iteracion3'
	echo ' 4 Iteracion4'
	echo ' 5 Iteracion5'
	echo ' 6 Iteracion6'
	echo ' 7 Actual'
	echo ' 8 Cancelar'
	echo 'Pulse el numero de Iteracion que desea instalar'
}

function alerta
{
	echo 'Opcion no valida, porfavor ingrese una opcion valida'
}

continuar=true
while [ $continuar == true ]
do
	iteracion
	read OPT
	case $OPT in
		1 )
			fuente="$iteracion1"
			echo 'Iteracion 1 seleccionado'
			nombre_fichero='Iteracion1'
			directorio='Iteracion1'
			continuar=false ;;
		2 )
			fuente="$iteracion2"
			echo 'Iteracion 2 seleccionado'
			nombre_fichero='tag-iteracion2'
			directorio='Iteracion2'
			continuar=false ;;
		3 )
			fuente="$iteracion3"
			echo 'Iteracion 3 seleccionado'
			nombre_fichero='iteracion3'
			directorio='Iteracion3'
			continuar=false ;;
		4 )
			fuente="$iteracion4"
			echo 'Iteracion 4 seleccionado'
			nombre_fichero='iteracion4'
			directorio='Iteracion4'
			continuar=false ;;
		5 )
			fuente="$iteracion5"
			echo 'Iteracion 5 seleccionado'
			nombre_fichero='iteracion5'
			directorio='Iteracion5'
			continuar=false ;;
		6 )
			fuente="$iteracion6"
			echo 'Iteracion 6 seleccionado'
			nombre_fichero='iteracion6'
			directorio='Iteracion6'
			continuar=false ;;
		7 )
			fuente="$actual"
			echo 'Ultima version del proyecto seleccionada'
			nombre_fichero='master'
			directorio='Iteracion7'
			continuar=false ;;
		8 )
			exit ;;
		? ) clear && alerta;;
	esac
done

#Detectamos si tenemos conexion a internet para continuar con la instalacion
gnome-terminal -x bash -c "ping -c 1 www.google.com > red.txt"
conexion=`grep 'PING www.google.com' red.txt`
rm red.txt
if [ -z "$conexion" ];
	then
	echo "IMPOSIBLE CONTINUAR CON LA INSTALACION, DEBE ASEGURARSE DE TENER UNA CONEXION A INTERNET"
	exit
fi

if [ ! -d "$rutainstalacion" ];
	then
	echo "###### LA RUTA DE INSTALACION NO EXISTE, SE CREARA EL DIRECTORIO EN LA RUTA ESPECIFICADA ######"
	mkdir -p "$rutainstalacion"
fi

#instalamos zlib1g-dev
instalado=`dpkg -l | grep zlib1g-dev`
if [ -n "$instalado" ];
	then
	echo "zlib1g-dev ya esta instalado"
else
	apt-get install zlib1g-dev
fi

# instalamos python 2.7.4
instalado=`dpkg -l | grep python2.7`
if [ -n "$instalado" ];
	then
	echo "python2.7 ya esta instalado"
else
	echo "Instalamos python2.7..."
	cd paquetes
	tar -Jxf Python-2.7.4.tar.xz
	cd Python-2.7.4
	./configure
	make
	make install
	cd ..
	rm -rf Python-2.7.4
	cd ..
fi

#python-setuptools
instalado=`dpkg -l | grep python-setuptools`
if [ -n "$instalado" ];
	then
	echo "python-setuptools ya esta instalada"
else
	echo "Instalamos la libreria python-setuptools"
	apt-get -y install python-setuptools
fi

#python-dev
instalado=`dpkg -l | grep python-dev`
if [ -n "$instalado" ];
	then
	echo "python-dev ya esta instalada"
else
	echo "Instalamos la libreria python-dev"
	apt-get -y install python-dev
fi

#Django
if [ -d /usr/local/lib/python2.7/dist-packages/django ];
	then
	echo "Django ya esta instalado"
else
	#instalamos el framework Django
	echo "Instalamos el framework Django"
	cd paquetes
	tar xzvf Django-1.6.2.tar.gz
	cd Django-1.6.2
	python setup.py install
	cd ..
	rm -rf Django-1.6.2
	cd ..
fi

#unipath
if [ -d /usr/local/lib/python2.7/dist-packages/unipath ];
	then
	echo "unipath ya esta instalado"
else
	#instalamos el framework Django
	echo "Instalamos la libreria unipath"
	cd paquetes
	tar xzvf Unipath-1.0.tar.gz
	cd Unipath-1.0
	python setup.py install
	cd ..
	rm -rf Unipath-1.0
fi

#apache
instalado=`dpkg -l | grep apache2`
if [ -n "$instalado" ];
	then
	echo "apache2 ya esta instalado"
else
	echo "Instalamos apache2"
	apt-get -y install apache2
fi

#libapache2
instalado=`dpkg -l | grep libapache2`
if [ -n "$instalado" ];
	then
	echo "libapache2 ya esta instalada"
else
	echo "Instalamos la libreria libapache2"
	apt-get -y install libapache2-mod-wsgi
fi


# instalamos los complementos necesarios para el paquete pisa para ello desempaquetamos los paquetes, instalamos y borramos los directorios que contienen los archivos de instalacion descomprimdos, realizamos esta accion para cada paquete.

# intalamos html5lib-0.90
if [ -d /usr/local/lib/python2.7/dist-packages/html5lib-0.90-py2.7.egg ];
	then
	echo "html5lib-0.90 ya esta instalado"
else
	echo "Instalamos html5lib-0.90..."
	cd paquetes
	tar xzvf html5lib-0.90.tar.gz
	cd html5lib-0.90
	python setup.py install
	cd ..
	rm -rf html5lib-0.90
	cd ..
fi

# instalamos reportlab
instalado=`dpkg -l | grep reportlab`
if [ -n "$instalado" ];
	then
	echo "reportlab ya esta instalada"
else
	echo "Instalamos reportlab..."
	cd paquetes
	tar xzvf reportlab-3.1.8.tar.gz
	cd reportlab-3.1.8
	python setup.py install
	cd ..
	rm -rf reportlab-3.1.8
	cd ..
fi

# instalamos PIL
if [ -d /usr/local/lib/python2.7/dist-packages/PIL ];
	then
	echo "PIL ya esta instalado"
else
	echo "Instalamos PIL..."
	cd paquetes
	tar xzvf Imaging-1.1.7.tar.gz
	cd Imaging-1.1.7
	python setup.py install
	cd ..
	rm -rf Imaging-1.1.7
	cd ..
fi

# instalamos pyPdf
if [ -d /usr/local/lib/python2.7/dist-packages/pyPdf ];
	then
	echo "pyPdf ya esta instalado"
else
	echo "Instalamos pyPdf..."
	cd paquetes
	tar xzvf pyPdf-1.10.tar.gz
	cd pyPdf-1.10
	python setup.py install
	cd ..
	rm -rf pyPdf-1.10
	cd ..
fi

# finalmente instalamos pisa
if [ -d /usr/local/lib/python2.7/dist-packages/pisa-3.0.33-py2.7.egg ];
	then
	echo "pisa ya esta instalado"
else
	echo "Instalamos pisa..."
	cd paquetes
	tar xzvf pisa-3.0.33.tar.gz
	cd pisa-3.0.33
	python setup.py install
	cd ..
	rm -rf pisa-3.0.33
	cd ..
fi

# instalamos django-cron-0.3.3
if [ -d /usr/local/lib/python2.7/dist-packages/django_cron-0.3.3-py2.7.egg ];
	then
	echo "django-cron-0.3.3 ya esta instalado"
else
	echo "Instalamos django-cron-0.3.3..."
	cd paquetes
	tar xzvf django-cron-0.3.3.tar.gz
	cd django-cron-0.3.3
	python setup.py install
	cd ..
	rm -rf django-cron-0.3.3
	cd ..
fi

# instalamos erlang-solutions_1.0_all
instalado=`dpkg -l | grep erlang-solutions`
if [ -n "$instalado" ];
	then
	echo "erlang-solutions ya esta instalado"
else
	echo "Instalamos django-cron-0.3.3..."
	cd paquetes
	sudo dpkg -i erlang-solutions_1.0_all.deb
	#sudo apt-get update
	sudo apt-get -y install erlang
	rm -rf erlang-solutions_1.0_all
	cd ..	
fi

# instalamos RabbitMQ-Server
instalado=`dpkg -l | grep rabbitmq-server`
if [ -n "$instalado" ];
	then
	echo "RabbitMQ-Server ya esta instalado"
else
	echo "Instalamos RabbitMQ-Server..."
	cd paquetes
	sudo dpkg -i rabbitmq-server_3.3.2-1_all.deb
	sudo apt-get -y -f install rabbitmq-server
	sudo apt-get -y -f install
	rm -rf rabbitmq-server_3.3.2-1_all
	cd ..
fi

# instalamos Celery
if [ -d /usr/local/lib/python2.7/dist-packages/celery-3.1.12-py2.7.egg ];
	then
	echo "Celery ya esta instalado"
else
	#instalamos Celery
	echo "Instalamos Celery..."
	cd paquetes
	tar xzvf celery-3.1.12.tar.gz
	cd celery-3.1.12
	python setup.py install
	cd ..
	rm -rf celery-3.1.12
	cd ..
fi

# instalamos Django-Celery
if [ -d /usr/local/lib/python2.7/dist-packages/django_celery-3.1.10-py2.7.egg ];
	then
	echo "Django-Celery ya esta instalado"
else
	
	sudo pip install django-celery

	#instalamos Django-Celery
	echo "Instalamos Django-Celery..."
	cd paquetes
	tar xzvf django-celery-3.1.10.tar.gz
	cd django-celery-3.1.10
	python setup.py install
	cd ..
	rm -rf django-celery-3.1.10
	cd ..
fi

sudo rabbitmqctl add_user sap sap
sudo rabbitmqctl add_vhost sap
sudo rabbitmqctl set_permissions -p sap sap ".*" ".*" ".*"

#proyecto
if [ -d "$rutainstalacion/$directorio/sap" ];
	then
	echo "La iteracion del proyecto seleccionado ya se encuentra instalado"

else
	mkdir -p "$rutainstalacion/$directorio"
	if [ -d proyecto ];
		then
		rm -rf proyecto
	fi

	wget "$fuente" -P proyecto
	cd proyecto
	unzip "$nombre_fichero".zip
	cd is2_git-"$nombre_fichero"
	mv * "$rutainstalacion/$directorio/"
	cd "$rutainstalacion/$directorio/"
	chown "$usuario" sap README.md
	chmod -R 777 "$rutainstalacion"
	cd "$rutainstalador"
	rm -rf proyecto
fi

#archivo sap.wsgi
ruta_sap_wsgi="$rutainstalacion/$directorio/sap"
instalado=`ls "$ruta_sap_wsgi" | grep sap.wsgi`
if [ -n "$instalado" ];
then
	echo "borrando el archivo sap.wsgi existente en el proyecto"
	rm "$ruta_sap_wsgi/sap.wsgi"
fi
echo "creando el archivo sap.wsgi"
echo "import os" > sap.wsgi
echo "import sys" >> sap.wsgi
echo "sys.path = ['"$ruta_sap_wsgi"'] + sys.path" >> sap.wsgi
echo "os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'" >> sap.wsgi
echo "import django.core.handlers.wsgi" >> sap.wsgi
echo "application = django.core.handlers.wsgi.WSGIHandler()" >> sap.wsgi
echo "moviendo el archivo sap.wsgi al proyecto..."
mv sap.wsgi "$ruta_sap_wsgi"
chown mdrm016 "$ruta_sap_wsgi/sap.wsgi"
chmod +x "$ruta_sap_wsgi/sap.wsgi"
echo "archivo sap.wsgi movido"

#archivo sap.conf
ruta_sap_conf="/etc/apache2/sites-available"
instalado=`ls "$ruta_sap_conf" | grep sap.conf`
if [ -n "$instalado" ];
then
	
	echo "borrando el archivo sap.conf existente en $ruta_sap_conf"
	rm "$ruta_sap_conf/sap.conf"
fi
echo "creando el archivo sap.conf"
echo "<VirtualHost *:80>" > sap.conf
echo "WSGIScriptAlias / $ruta_sap_wsgi/sap.wsgi" >> sap.conf
echo "" >> sap.conf
echo "ServerName sap.com" >> sap.conf
echo "Alias /static $ruta_sap_wsgi/static/" >> sap.conf
echo "" >> sap.conf
echo "<Directory $ruta_sap_wsgi>" >> sap.conf
echo "Order allow,deny" >> sap.conf
echo "Allow from all" >> sap.conf
echo "</Directory>" >> sap.conf
echo "</VirtualHost>" >> sap.conf
echo "moviendo el archivo sap.conf en $ruta_sap_conf"
mv sap.conf "$ruta_sap_conf"
echo "archivo sap.conf movido"
echo "activando el servidor apache con django..."
cd /etc/apache2/sites-available/
a2ensite sap.conf
/etc/init.d/apache2 restart
cd "$rutainstalador"
echo "servidor apache activado"

#archivo hosts
instalado=`grep sap.com /etc/hosts`
if [ -n "$instalado" ];
	then
	echo "el link sap.com ya esta activado"
else
	echo "activando el link sap.com..."
	echo '' >> /etc/hosts
	echo '127.0.1.1       sap.com' >> /etc/hosts
	/etc/init.d/apache2 restart
	echo "el link sap.com activado"
fi

#postgresql
instalado=`dpkg -l | grep postgresql`
if [ -n "$instalado" ];
	then
	echo "postgresql ya esta instalado"
else
	echo "Instalamos postgresql..."
	apt-get -y install postgresql postgresql-client postgresql-contrib
fi

#python-psycopg2
instalado=`dpkg -l | grep python-psycopg2`
if [ -n "$instalado" ];
	then
	echo "python-psycopg2 ya esta instalado"
	sudo -u postgres dropdb sap
	sudo -u postgres createdb -O sap sap
	sudo -u postgres dropdb sap_desarrollo
	sudo -u postgres createdb -O sap sap_desarrollo
else
	echo "Instalamos python-psycopg2..."
	apt-get -y install python-psycopg2

	chmod 777 -R /home/"$usuario"
	echo "ALTER USER postgres WITH PASSWORD 'postgres';" > comandos.sql
	echo "\q" >> comandos.sql
	sudo -u postgres psql -a -f comandos.sql
	sudo -u postgres createuser --superuser "$usuario"
	echo "ALTER USER "$usuario" WITH PASSWORD '"$password"';" > comandos.sql
	echo "\q" >> comandos.sql
	sudo -u postgres psql -a -f comandos.sql
	sudo -u postgres createuser -d -a sap
	echo "ALTER USER sap WITH PASSWORD 'sap';" > comandos.sql
	echo "\q" >> comandos.sql
	sudo -u postgres psql -a -f comandos.sql
	rm comandos.sql	
	sudo -u postgres createdb -O sap sap
	sudo -u postgres createdb -O sap sap_desarrollo
fi


#syncdb
echo "import os
import sys
from unipath import Path" > syncdb.py

echo "p = Path('$rutainstalacion/$directorio/sap')" >> syncdb.py

echo "sys.path = [p] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'sap.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.contrib.auth.management.commands import changepassword
from django.core import management

# Run the syncdb
management.call_command('syncdb', interactive=False)

# Create the super user and sets his password.
management.call_command('createsuperuser', interactive=False, username='sap', email='sap@sap.com')
command = changepassword.Command()
command._get_pass = lambda *args: 'sap'
command.execute('sap')" >> syncdb.py
python syncdb.py
rm syncdb.py

cd "$rutainstalacion/$directorio/sap"
su "$usuario" -c "gnome-terminal -x bash -c 'python manage.py celeryd --verbosity=2 --loglevel=DEBUG && python manage.py celerybeat --verbosity=2 --loglevel=DEBUG'"

echo "###### INSTALACION FINALIZADA, LANZANDO EL NAVEGADOR ######"
su "$usuario" -c 'firefox -new-tab sap.com &'
#su "$usuario" -c 'google-chrome -new-tab sap.com &'
#su "$usuario" -c 'chromium-browser -new-tab sap.com &'
