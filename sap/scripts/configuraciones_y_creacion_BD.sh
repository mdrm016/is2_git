#! /bin/bash 

clear

echo "*****************Creando Usuario sapAdmin*****************"
cd /home/eduardo/workspace/is2_git/sap/scripts/
createuser -d -a sap
createdb -O sap sap
psql -d sap -a -f pass.sql

