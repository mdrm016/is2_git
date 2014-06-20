#!/bin/bash
dropdb sap_desarrollo
createdb -O sap sap_desarrollo
sed -i 's/''sap_produccion''/''sap_desarrollo''/g' /home/ysapy/workspace/is2_git/sap/sap/settings.py
sudo rm -rf poblacion_produccion.sql
pg_dump -c sap_produccion > poblacion_produccion.sql
cat poblacion_desarrollo.sql | psql sap_desarrollo
sudo /etc/init.d/apache2 restart
