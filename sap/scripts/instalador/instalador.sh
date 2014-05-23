#! /bin/bash

#variables
#ruta de instalacion
rutainstalacion="/home/mdrm016/is2_git/is2_git"
#nombre del superusuario a crear en la BD
usuario='mdrm016'
#password del super usuario a crear en la BD
password='444444666666'
#ruta actual del instalador
rutainstalador=`pwd`
#localizacion del codigo fuente del proyecto
fuente="https://github.com/mdrm016/is2_git/archive/master.zip"
#paquetes instalados actualmente
apt-show-versions > instalados.txt

if [ ! -d "$rutainstalacion" ];
	then
	echo "###### LA RUTA DE INSTALACION NO EXISTE, SE CREARA EL DIRECTORIO EN LA RUTA ESPECIFICADA ######"
	mkdir -p "$rutainstalacion"
fi

echo "###### INICIANDO LA INSTALACION DEL SISTEMA DE ADMINISTRACION DE PROYECTOS (SAP) ######"

# instalamos python 2.7.4
instalado=`grep python2.7 instalados.txt`
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
instalado=`grep python-setuptools instalados.txt`
if [ -n "$instalado" ];
	then
	echo "la libreria python-setuptools ya esta instalada"
else
	echo "Instalamos la libreria python-setuptools"
	apt-get -y install python-setuptools
fi

#python-dev
instalado=`grep python-dev instalados.txt`
if [ -n "$instalado" ];
	then
	echo "la libreria python-dev ya esta instalada"
else
	echo "Instalamos la libreria python-dev"
	apt-get install -y python-dev
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
instalado=`grep apache2 instalados.txt`
if [ -n "$instalado" ];
	then
	echo "apache2 ya esta instalado"
else
	echo "Instalamos apache2"
	apt-get -y install apache2
fi

#libapache2
instalado=`grep libapache2 instalados.txt`
if [ -n "$instalado" ];
	then
	echo "la libreria libapache2 ya esta instalada"
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
instalado=`grep reportlab instalados.txt`
if [ -n "$instalado" ];
	then
	echo "la libreria reportlab ya esta instalada"
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

#proyecto
if [ -d "$rutainstalacion/sap" ];
	then
	echo "El proyecto ya se encuentra instalado"
else 
	if [ ! -d proyecto ];
		then
		wget "$fuente" -P proyecto
	fi
	cd proyecto
	unzip master.zip
	cd is2_git-master
	mv * "$rutainstalacion"
	cd "$rutainstalacion"
	chown mdrm016 sap README.md
	chmod -R 777 sap
	cd sap/static
	chmod -R a+w uploads
	cd aplicaciones
	chmod a+w informes
	cd "$rutainstalador"
	rm -rf proyecto
	wsgi_conf="yes"
fi

#archivo sap.wsgi
ruta_sap_wsgi="$rutainstalacion/sap"
instalado=`ls "$ruta_sap_wsgi" | grep sap.wsgi`
if [ -n "$instalado" ];
	then
	if [ -n "$wsgi_conf" ];
	then
		echo "borrando el archivo sap.wsgi existente en el proyecto"
		rm "$ruta_sap_wsgi/sap.wsgi"
	else
		echo "el archivo sap.wsgi ya existe en el proyecto"
	fi
fi
if [ -n "$wsgi_conf" ];
	then
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
fi

#archivo sap.conf
ruta_sap_conf="/etc/apache2/sites-available"
instalado=`ls "$ruta_sap_conf" | grep sap.conf`
if [ -n "$instalado" ];
	then
	if [ -n "$wsgi_conf" ];
	then
		echo "borrando el archivo sap.conf existente en $ruta_sap_conf"
		rm "$ruta_sap_conf/sap.conf"
	else 
		echo "el archivo sap.conf ya existe en $ruta_sap_conf"
	fi
fi
if [ -n "$wsgi_conf" ];
	then
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
fi

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
instalado=`grep postgresql instalados.txt`
if [ -n "$instalado" ];
	then
	echo "postgresql ya esta instalado"
else
	echo "Instalamos postgresql..."
	apt-get -y install postgresql postgresql-client postgresql-contrib

	#python-psycopg2
	instalado=`grep python-psycopg2 instalados.txt`
	if [ -n "$instalado" ];
		then
		echo "python-psycopg2 ya esta instalado"
	else
		echo "Instalamos python-psycopg2..."
		apt-get -y install python-psycopg2
	fi

	echo "ALTER USER postgres WITH PASSWORD 'postgres';" > comandos.sql
	echo "\q" >> comandos.sql
	sudo -u postgres psql postgres -a -f comandos.sql
	sudo -u postgres createuser --superuser mdrm016
	echo "ALTER USER "$usuario" WITH PASSWORD '"$password"';" > comandos.sql
	echo "\q" >> comandos.sql
	sudo -u postgres psql -a -f comandos.sql
	sudo -u postgres createuser -d -a sap
	echo "ALTER USER sap WITH PASSWORD 'sap';" > comandos.sql
	echo "\q" >> comandos.sql
	sudo -u postgres psql -a -f comandos.sql
	sudo -u postgres createdb -O sap sap_desarrollo
	rm comandos.sql
	python syncdb.py	
fi

rm instalados.txt

echo "###### INSTALACION FINALIZADA, LANZANDO EL NAVEGADOR ######"
firefox -new-tab sap.com
#google-chrome -new-tab sap.com
#chromium-browser -new-tab sap.com
