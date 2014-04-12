#! /bin/bash 

clear

echo "*****************Creando Usuario sapAdmin*****************"
sudo -u postgres psql postgres
sudo -u postgres createuser sap
n
n
n
sudo -u postgres psql
\password sap
sap
sap

echo "*****************Creando Base de Datos sap*****************"
createdb -O sap sap
yes
SapAdmin
sap@sap.com
sapAdmin
sapAdmin

echo "*****************Sincronizando la Base de Datos*****************"
cd ..
python manage.py syncdb

