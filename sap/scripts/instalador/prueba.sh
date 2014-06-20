#!/bin/bash

# instalamos pyparsing-1.5.7
if [ -f /usr/local/lib/python2.7/dist-packages/pyparsing.py ];
	then
	echo "pyparsing-1.5.7 ya esta instalado"
else

	#instalamos pyparsing-1.5.7
	echo "Instalamos pyparsing-1.5.7..."
	cd paquetes
	tar xzvf pyparsing-1.5.7.tar.gz
	cd pyparsing-1.5.7
	python setup.py install
	cd ..
	rm -rf pyparsing-1.5.7
	cd ..
fi

# instalamos pydot-1.0.2
if [ -d /usr/local/lib/python2.7/dist-packages/pydot-1.0.2-py2.7.egg ];
	then
	echo "pydot-1.0.2 ya esta instalado"
else

	#instalamos pydot-1.0.2
	echo "Instalamos pydot-1.0.2..."
	cd paquetes
	tar xzvf pydot-1.0.2.tar.gz
	cd pydot-1.0.2
	python setup.py install
	cd ..
	rm -rf pydot-1.0.2
	cd ..
fi

# instalamos graphviz
instalado=`dpkg -l | grep graphviz`
if [ -n "$instalado" ];
	then
	echo "graphviz ya esta instalado"
else
	echo "Instalamos graphviz..."
	sudo apt-get -y install graphviz

fi
